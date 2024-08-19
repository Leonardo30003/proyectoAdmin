import reflex as rx
from datetime import datetime

# Estado para manejar la creación de horarios
class ScheduleState(rx.State):
    teacher_name: str = ""
    subject: str = ""
    day: str = ""
    start_time: str = ""
    end_time: str = ""

    def handle_change(self, key: str, value: str):
        setattr(self, key, value)

    def handle_submit(self):
        schedule_entry = {
            "teacher_name": self.teacher_name,
            "subject": self.subject,
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        print("Nuevo horario creado:", schedule_entry)
        rx.window_alert("Horario creado exitosamente.")

@rx.page(
    route="/crear_horario",
    title="Crear Horario",
)
def create_schedule_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading(
                    "Crear Horario para Docente",
                    size="2.5em",
                    color="#910048",
                    text_align="center",
                    width="100%",
                    margin_bottom="1rem",
                ),
                rx.box(
                    rx.text("Nombre del Docente", color="#555555", margin_bottom="0.5rem"),
                    rx.input(
                        placeholder="Nombre del Docente",
                        on_change=lambda value: ScheduleState.handle_change("teacher_name", value),
                        padding="0.5rem",
                        border="1px solid #dddddd",
                        border_radius="0.5rem",
                        background_color="#F8F8F8",
                        color="#333333",
                        font_size="1rem",
                        margin_bottom="1rem",
                    ),
                    width="100%"
                ),
                rx.box(
                    rx.text("Materia", color="#555555", margin_bottom="0.5rem"),
                    rx.input(
                        placeholder="Materia",
                        on_change=lambda value: ScheduleState.handle_change("subject", value),
                        padding="0.5rem",
                        border="1px solid #dddddd",
                        border_radius="0.5rem",
                        background_color="#F8F8F8",
                        color="#333333",
                        font_size="1rem",
                        margin_bottom="1rem",
                    ),
                    width="100%"
                ),
                rx.box(
                    rx.text("Día", color="#555555", margin_bottom="0.5rem"),
                    rx.select(
                        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
                        placeholder="Seleccione un día",
                        on_change=lambda value: ScheduleState.handle_change("day", value),
                        padding="0.5rem",
                        border="1px solid #dddddd",
                        border_radius="0.5rem",
                        background_color="#F8F8F8",
                        color="#333333",
                        font_size="1rem",
                        margin_bottom="1rem",
                        width="100%",
                    ),
                ),
                rx.box(
                    rx.text("Hora de Inicio", color="#555555", margin_bottom="0.5rem"),
                    rx.input(
                        type="time",
                        on_change=lambda value: ScheduleState.handle_change("start_time", value),
                        padding="0.5rem",
                        border="1px solid #dddddd",
                        border_radius="0.5rem",
                        background_color="#F8F8F8",
                        color="#333333",
                        font_size="1rem",
                        margin_bottom="1rem",
                        width="100%",
                    ),
                ),
                rx.box(
                    rx.text("Hora de Fin", color="#555555", margin_bottom="0.5rem"),
                    rx.input(
                        type="time",
                        on_change=lambda value: ScheduleState.handle_change("end_time", value),
                        padding="0.5rem",
                        border="1px solid #dddddd",
                        border_radius="0.5rem",
                        background_color="#F8F8F8",
                        color="#333333",
                        font_size="1rem",
                        margin_bottom="1.5rem",
                        width="100%",
                    ),
                ),
                rx.button(
                    "Crear Horario",
                    on_click=ScheduleState.handle_submit,
                    background="#001737",
                    color="white",
                    padding="0.5rem 1.5rem",
                    border_radius="0.75rem",
                    box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                    _hover={
                        "background": "#FF011D",
                        "box_shadow": "0 6px 12px rgba(0, 0, 0, 0.3)"
                    },
                    width="100%",
                ),
                spacing="1.5rem",
                width="100%",
            ),
            padding="3rem",
            background_color="#FFFFFF",
            border_radius="1rem",
            box_shadow="0 5px 20px rgba(0, 0, 0, 0.1)",
        ),
        height="100vh",
        background_color="#F0F0F0",
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(create_schedule_page)
    app.compile()
