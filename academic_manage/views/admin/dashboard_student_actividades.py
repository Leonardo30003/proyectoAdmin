import reflex as rx

# Datos de ejemplo para las calificaciones
grades_data = {
    "Matemáticas": [
        {"task": "Examen 1", "date": "2024-05-10", "grade": "A"},
        {"task": "Tarea 2", "date": "2024-05-15", "grade": "B+"},
    ],
    "Ciencias": [
        {"task": "Proyecto 1", "date": "2024-05-12", "grade": "A-"},
        {"task": "Examen 2", "date": "2024-05-20", "grade": "B"},
    ],
    "Historia": [
        {"task": "Ensayo 1", "date": "2024-05-18", "grade": "A"},
        {"task": "Examen 1", "date": "2024-05-25", "grade": "B+"},
    ],
    "Inglés": [
        {"task": "Examen Oral", "date": "2024-05-22", "grade": "A"},
        {"task": "Examen 2", "date": "2024-05-30", "grade": "A-"},
    ],
}

# Datos de ejemplo para el horario
schedule = {
    "Lunes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
    "Martes": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
    "Miércoles": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
    "Jueves": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
    "Viernes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
}

# Estado para manejar la selección de materias y navegación
class GradeState(rx.State):
    selected_subject: str = ""

    def set_subject(self, subject):
        self.selected_subject = subject

    def navigate(self, route: str):
        return rx.redirect(route)

# Información del estudiante
student_info = {
    "name": "Juan Pérez",
    "course": "Curso: 10mo Grado - Sección A",
}

@rx.page(
    route="/materias",
    title="Materias",
)
def materias_page() -> rx.Component:
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
        {"label": "Horarios", "active": False, "route": "/horario"},
        {"label": "Calificaciones", "active": True, "route": "/materias"},
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
            background="#001737" if not item["active"] else "#FF011D",  # Cambios de color para activo/inactivo
            border_radius="10px",
            margin_bottom="1em",
            cursor="pointer",
            transition="background 0.3s, transform 0.3s",
            _hover={
                "background": "#FF011D",  # Hover rojo
                "transform": "scale(1.05)",
            },
            on_click=lambda: GradeState.navigate(item["route"]),
        )
    
    # Datos para las materias
    subjects = [
        {"title": "Matemáticas", "description": "Resolver los ejercicios de la página 42"},
        {"title": "Historia", "description": "Leer el capítulo 5 y responder las preguntas"},
        {"title": "Ciencias", "description": "Preparar una presentación sobre el ciclo del agua"},
        {"title": "Inglés", "description": "Escribir un ensayo sobre tu libro favorito"},
    ]
    
    # Función para renderizar cada tarjeta de materia
    def subject_card(subject):
        return rx.box(
            rx.text(subject["title"], font_size="1.2em", color="#FFFFFF", text_align="center"),
            rx.text(subject["description"], font_size="1em", color="#AAAAAA", text_align="center"),
            width="200px",
            height="100px",
            margin="0.5em",
            padding="1em",
            background="linear-gradient(135deg, #FF011D 0%, #000000 100%)",  # Gradiente de rojo a negro
            border_radius="10px",
            box_shadow="0 5px 10px rgba(0, 0, 0, 0.2)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
            transition="transform 0.3s",
            cursor="pointer",
            _hover={
                "transform": "translateY(-5px)",
            },
            on_click=lambda: GradeState.set_subject(subject["title"]),
        )
    
    # Renderizar la tabla de calificaciones
    def grades_table():
        return rx.cond(
            GradeState.selected_subject != "",
            rx.box(
                rx.text(f"Calificaciones para {GradeState.selected_subject}", font_size="1.5em", font_weight="bold", color="#FFFFFF", margin_bottom="1em"),
                rx.grid(
                    rx.grid(
                        rx.text("Tarea", font_weight="bold", padding="0.5em", color="#FFFFFF"),
                        rx.text("Fecha", font_weight="bold", padding="0.5em", color="#FFFFFF"),
                        rx.text("Calificación", font_weight="bold", padding="0.5em", color="#FFFFFF"),
                        columns="repeat(3, 1fr)",
                        background="#3A3A3A",
                        padding="1em",
                        border_radius="10px",
                    ),
                    *[
                        rx.grid(
                            rx.text(grade["task"], padding="0.5em", color="#FFFFFF"),
                            rx.text(grade["date"], padding="0.5em", color="#FFFFFF"),
                            rx.text(grade["grade"], padding="0.5em", color="#FFFFFF"),
                            columns="repeat(3, 1fr)",
                            background="#2A2A2A",
                            padding="1em",
                            border_radius="10px",
                            margin_top="0.5em",
                        )
                        for grade in grades_data.get(GradeState.selected_subject, [])
                    ],
                    width="100%",
                    background="#2A3B4C",
                    border_radius="10px",
                    box_shadow="0 10px 15px rgba(0, 0, 0, 0.2)",
                    color="white",
                    padding="1em",
                ),
                width="100%",
                padding="1em",
                background="linear-gradient(to bottom right, #FF011D, #000000)",  # Fondo de la tabla de rojo a negro
                border_radius="15px",
                box_shadow="0 10px 20px rgba(0, 0, 0, 0.3)",
            ),
            rx.text("Seleccione una materia para ver las calificaciones", font_size="1.5em", color="#FFFFFF", text_align="center", margin_top="2em")
        )

    # Composición de la página
    return rx.box(
        navbar,
        rx.box(
            rx.box(
                *[sidebar_item(item) for item in sidebar_items],
                width="15%",
                background="#001737",  # Fondo azul oscuro de la barra lateral
                padding="1em",
                box_shadow="2px 0 10px rgba(0, 0, 0, 0.15)",
                border_radius="10px",
                display="flex",
                flex_direction="column",
                align_items="center",
                height="100%",
            ),
            rx.box(
                rx.box(
                    *[subject_card(subject) for subject in subjects],
                    display="flex",
                    flex_direction="column",
                    justify_content="space-between",
                    height="100%",
                    padding="1em",
                    background="linear-gradient(to bottom right, #FF011D, #000000)",  # Fondo de rojo a negro
                    border_radius="15px",
                    box_shadow="0 10px 20px rgba(0, 0, 0, 0.3)",
                    margin_right="1em",
                ),
                grades_table(),
                display="flex",
                flex_direction="row",
                width="85%",
                height="100%",
                padding="2em",
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
    app.add_page(materias_page)
    app.compile()
