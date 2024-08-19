import reflex as rx
from ..views.asignacion_tareas import asignar_tarea_page

@rx.page(
    route="/dashboard_docente",
    title=" Dashboard del Docente",
)
def cursos_page() -> rx.Component:
    # Datos para la barra lateral
    sidebar_items = [
        {"label": "Cursos", "active": True},
        {"label": "Horarios", "active": False},
        {"label": "Calificaciones", "active": False},
        {"label": "Actividades", "active": False},
    ]
    
    # Función para renderizar cada ítem de la barra lateral
    def sidebar_item(item):
        return rx.box(
            rx.text(
                item["label"], 
                font_size="1.2em", 
                color="white",
                font_weight="bold",
                padding="1em"
            ),
            background="#2A3B4C" if not item["active"] else "#48CAE4",
            border_radius="10px",
            margin_bottom="1em",
            cursor="pointer",
            transition="background 0.3s, transform 0.3s",
            _hover={
                "background": "#48CAE4",
                "transform": "scale(1.05)",
            },
        )
    
    # Datos para los cursos
    courses = [
        {"name": "Matemáticas", "description": "Curso avanzado de álgebra y cálculo", "teacher": "Prof. García"},
        {"name": "Ciencias", "description": "Biología y Química para secundaria", "teacher": "Dra. López"},
        {"name": "Historia", "description": "Historia universal desde la antigüedad hasta la modernidad", "teacher": "Prof. Pérez"},
        {"name": "Inglés", "description": "Curso de inglés intermedio", "teacher": "Prof. Smith"},
    ]
    
    # Función para renderizar cada tarjeta de curso
    def course_card(course):
        return rx.box(
            rx.text(course["name"], font_size="1.5em", color="white", font_weight="bold"),
            rx.text(course["description"], font_size="1em", color="white"),
            rx.text(f"Profesor: {course['teacher']}", font_size="1em", color="#CCCCCC"),
            rx.button("Asignar Tarea", on_click=lambda: rx.redirect("/asignar_tarea"), margin_top="1em"),
            padding="1.5em",
            background="linear-gradient(135deg, #3A6073 0%, #16222A 100%)",
            border_radius="10px",
            box_shadow="0 10px 15px rgba(0, 0, 0, 0.2)",
            text_align="left",
            display="flex",
            flex_direction="column",
            transition="transform 0.3s",
            _hover={
                "transform": "translateY(-10px)",
            },
            width="300px",  # Ancho fijo para las tarjetas
            margin="1em",   # Margen para separar las tarjetas
        )
    
    # Composición de la página
    return rx.box(
        rx.box(
            *[sidebar_item(item) for item in sidebar_items],
            width="20%",
            background="#1A2B3C",
            padding="2em",
            box_shadow="2px 0 10px rgba(0, 0, 0, 0.15)",
            border_radius="15px",
        ),
        rx.box(
            *[course_card(course) for course in courses],
            display="flex",
            flex_wrap="wrap",  # Esto permite que las tarjetas se ajusten en filas y columnas
            justify_content="space-evenly",  # Distribuye uniformemente las tarjetas
            align_items="flex-start",
            width="80%",
            padding="2em",
            background="linear-gradient(to bottom right, #000428, #004e92)",
            border_radius="15px",
        ),
        display="flex",
        width="100%",
        height="100vh",
        padding="2em",
        background="#1E1E1E",
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(cursos_page)
    app.add_page(asignar_tarea_page) 
    app.compile()
