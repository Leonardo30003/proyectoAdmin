import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta
from ..models.assignmsent_model import Assignmsent

def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0
        if value == 0
        else float("inf")
    )
    return percentage_change


class MonthValues(rx.Base):
    """Values for a month."""

    num_assignments: int = 0
    total_points: float = 0.0
    num_completed: int = 0


class State(rx.State):
    """The app state."""

    assignments: list[Assignmsent] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_assignment: Assignmsent = Assignmsent()
    # Values for current and previous month
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()

    def load_entries(self) -> list[Assignmsent]:
        """Get all assignments from the database."""
        with rx.session() as session:
            query = select(Assignmsent)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Assignmsent, field).ilike(search_value)
                            for field in Assignmsent.get_fields()
                            if field not in ["id", "points"]
                        ],
                        # ensures that points is cast to a string before applying the ilike operator
                        cast(Assignmsent.points, String).ilike(search_value)
                    )
                )

            if self.sort_value:
                sort_column = getattr(Assignmsent, self.sort_value)
                if self.sort_value == "points":
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(func.lower(sort_column))
                query = query.order_by(order)

            self.assignments = session.exec(query).all()

        self.get_current_month_values()
        self.get_previous_month_values()

    def get_current_month_values(self):
        """Calculate current month's values."""
        now = datetime.now()
        start_of_month = datetime(now.year, now.month, 1)

        current_month_assignments = [
            assignment for assignment in self.assignments if datetime.strptime(assignment.date, '%Y-%m-%d %H:%M:%S') >= start_of_month
        ]
        num_assignments = len(current_month_assignments)
        total_points = sum(assignment.points for assignment in current_month_assignments)
        num_completed = len([assignment for assignment in current_month_assignments if assignment.status == "Completed"])
        self.current_month_values = MonthValues(num_assignments=num_assignments, total_points=total_points, num_completed=num_completed)

    def get_previous_month_values(self):
        """Calculate previous month's values."""
        now = datetime.now()
        first_day_of_current_month = datetime(now.year, now.month, 1)
        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
        start_of_last_month = datetime(last_day_of_last_month.year, last_day_of_last_month.month, 1)

        previous_month_assignments = [
            assignment for assignment in self.assignments
            if start_of_last_month <= datetime.strptime(assignment.date, '%Y-%m-%d %H:%M:%S') <= last_day_of_last_month
        ]
        # We add some dummy values to simulate growth/decline. Remove them in production.
        num_assignments = len(previous_month_assignments) + 3
        total_points = sum(assignment.points for assignment in previous_month_assignments) + 240
        num_completed = len([assignment for assignment in previous_month_assignments if assignment.status == "Completed"]) + 5

        self.previous_month_values = MonthValues(num_assignments=num_assignments, total_points=total_points, num_completed=num_completed)

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_assignment(self, assignment: Assignmsent):
        self.current_assignment = assignment

    def add_assignment_to_db(self, form_data: dict):
        self.current_assignment = form_data
        self.current_assignment["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with rx.session() as session:
            if session.exec(
                select(Assignmsent).where(Assignmsent.title == self.current_assignment["title"])
            ).first():
                return rx.window_alert("Assignment with this title already exists")
            session.add(Assignmsent(**self.current_assignment))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Assignment {self.current_assignment['title']} has been added.", variant="outline", position="bottom-right")

    def update_assignment_to_db(self, form_data: dict):
        self.current_assignment.update(form_data)
        with rx.session() as session:
            assignment = session.exec(
                select(Assignmsent).where(Assignmsent.id == self.current_assignment["id"])
            ).first()
            for field in Assignmsent.get_fields():
                if field != "id":
                    setattr(assignment, field, self.current_assignment[field])
            session.add(assignment)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Assignment {self.current_assignment['title']} has been modified.", variant="outline", position="bottom-right")

    def delete_assignment(self, id: int):
        """Delete an assignment from the database."""
        with rx.session() as session:
            assignment = session.exec(select(Assignmsent).where(Assignmsent.id == id)).first()
            session.delete(assignment)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Assignment {assignment.title} has been deleted.", variant="outline", position="bottom-right")

    @rx.var(cache=True)
    def points_change(self) -> float:
        return _get_percentage_change(self.current_month_values.total_points, self.previous_month_values.total_points)

    @rx.var(cache=True)
    def assignments_change(self) -> float:
        return _get_percentage_change(self.current_month_values.num_assignments, self.previous_month_values.num_assignments)

    @rx.var(cache=True)
    def completed_change(self) -> float:
        return _get_percentage_change(self.current_month_values.num_completed, self.previous_month_values.num_completed)
