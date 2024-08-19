import reflex as rx
from academic_manage.views.admin.dashboard_student_actividades import materias_page

# Estado para manejar la navegación de la barra lateral
class NavState(rx.State):
    def navigate(self, route):
        return rx.redirect(route)

@rx.page(
    route="/horario",
    title="Horario del Estudiante",
)
def horario_page() -> rx.Component:
    # Información del estudiante para el navbar
    student_info = {
        "name": "Juan Pérez",
        "course": "Curso: 10mo Grado - Sección A",
    }

    # Navbar con la información del estudiante
    navbar = rx.box(
        rx.text(f"Estudiante: {student_info['name']}", font_size="1.5em", color="#FFFFFF", padding_right="1em"),
        rx.text(student_info['course'], font_size="1.5em", color="#FFFFFF"),
        display="flex",
        justify_content="space-between",
        padding="1em 2em",
        background="#001737",  # Azul oscuro del logo
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
    )
    
    # Datos para la barra lateral
    sidebar_items = [
        {"label": "Horarios", "active": True, "route": "/horario"},
        {"label": "Calificaciones", "active": False, "route": "/materias"},  # Ajusta esta ruta según la definición de tu página de calificaciones
    ]
    
    # Función para renderizar cada ítem de la barra lateral
    def sidebar_item(item):
        return rx.box(
            rx.text(
                item["label"], 
                font_size="1.2em", 
                color="#FFFFFF",
                font_weight="bold",
                padding="1em"
            ),
            background="#001737" if not item["active"] else "#FF011D",
            border_radius="10px",
            margin_bottom="1em",
            cursor="pointer",
            transition="background 0.3s, transform 0.3s",
            _hover={
                "background": "#FF011D",  # Hover rojo
                "transform": "scale(1.05)",
            },
            on_click=lambda: NavState.navigate(item["route"]),
        )
    
    # Datos para el horario
    schedule = {
        "Lunes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
        "Martes": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
        "Miércoles": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
        "Jueves": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
        "Viernes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
    }
    
    # Función para renderizar cada columna de horario
    def schedule_column(day, classes):
        return rx.box(
            rx.text(day, font_size="1.5em", color="#FFFFFF", text_align="center", margin_bottom="1em"),
            *[
                rx.box(
                    rx.text(subject, font_size="1.2em", color="#FFFFFF", font_weight="bold"),
                    rx.text(time, font_size="1em", color="#AAAAAA"),
                    padding="1em",
                    background="linear-gradient(135deg, #FF011D 0%, #000000 100%)",
                    border_radius="10px",
                    box_shadow="0 10px 15px rgba(0, 0, 0, 0.2)",
                    margin_bottom="1em",
                    text_align="center",
                    display="flex",
                    flex_direction="column",
                    justify_content="center",
                    align_items="center",
                    transition="transform 0.3s",
                    _hover={
                        "transform": "translateY(-10px)",
                    },
                )
                for subject, time in classes
            ],
            width="180px",
            padding="1em",
            background="#001737",
            border_radius="15px",
            margin="1em",
        )
    
    # Composición de la página
    return rx.box(
        navbar,
        rx.box(
            rx.box(
                *[sidebar_item(item) for item in sidebar_items],
                width="15%",
                background="#001737",
                padding="1em",
                box_shadow="2px 0 10px rgba(0, 0, 0, 0.15)",
                border_radius="10px",
                display="flex",
                flex_direction="column",
                align_items="center",
                height="100%",
            ),
            rx.box(
                *[schedule_column(day, classes) for day, classes in schedule.items()],
                display="flex",
                justify_content="center",
                flex_wrap="wrap",
                width="85%",
                padding="2em",
                background="linear-gradient(to bottom right, #FF011D, #000000)",
                border_radius="15px",
                box_shadow="0 10px 20px rgba(0, 0, 0, 0.3)",
            ),
            display="flex",
            flex_direction="row",
            width="100%",
            height="100vh",
            padding="2em",
            background="#FFFFFF",  # Fondo blanco
        )
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(horario_page)
    app.compile()
