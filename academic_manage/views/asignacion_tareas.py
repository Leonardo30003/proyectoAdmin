import reflex as rx

class TaskState(rx.State):
    def publicar_tarea(self):
        # Aquí puedes añadir la lógica para procesar los datos si es necesario
        # Luego redirigir a la pantalla de cursos
        return rx.redirect("/cursos")

@rx.page(
    route="/asignar_tarea",
    title="Asignar Tarea",
)
def asignar_tarea_page() -> rx.Component:
    return rx.box(
        rx.text("Asignar Tarea", font_size="2em", font_weight="bold", margin_bottom="1em", color="#333"),
        rx.text_area(placeholder="Descripción de la tarea", width="100%", height="150px", margin_bottom="1em", style={"color": "#333"}),
        rx.input(placeholder="Ingrese el paralelo", width="100%", margin_bottom="1em", style={"color": "#333"}),
        rx.box(
            rx.text("Trimestre", margin_bottom="0.5em", color="#333"),
            rx.radio_group(
                items=["Trimestre 1", "Trimestre 2", "Trimestre 3"],
                default_value="Trimestre 1",
                direction="horizontal",
                spacing="1em",
                style={"color": "#333"},
            ),
            margin_bottom="1em",
        ),
        rx.box(
            rx.text("Tipo de Actividad", margin_bottom="0.5em", color="#333"),
            rx.radio_group(
                items=["Individual", "Grupal", "Proyecto", "Examen"],
                default_value="Individual",
                direction="horizontal",
                spacing="1em",
                style={"color": "#333"},
            ),
            margin_bottom="1em",
        ),
        rx.box(
            rx.text("Asignación de Actividades", margin_bottom="0.5em", color="#333"),
            rx.radio_group(
                items=["Lecciones", "Tareas", "Exposiciones", "Talleres"],
                default_value="Tareas",
                direction="horizontal",
                spacing="1em",
                style={"color": "#333"},
            ),
            margin_bottom="1em",
        ),
        rx.button("Publicar Tarea", background="#333", color="white", width="100%", margin_bottom="1em", on_click=TaskState.publicar_tarea),
        rx.button("Cancelar", variant="outline", width="100%", border_color="#333", color="#333",on_click=lambda: rx.redirect("/dashboard_docente")),
        width="50%",
        margin="auto",
        padding="2em",
        border_radius="10px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
        background="white"
    )

@rx.page(
    route="/cursos",
    title="Cursos",
)
def cursos_page() -> rx.Component:
    return rx.box(
        rx.text("¡Tarea publicada con éxito!", font_size="2em", font_weight="bold", color="#333", text_align="center"),
        rx.button("Volver al inicio", on_click=lambda: rx.redirect("/"), margin_top="2em", width="100%"),
        width="50%",
        margin="auto",
        padding="2em",
        border_radius="10px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
        background="white",
        text_align="center"
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(asignar_tarea_page)
    app.add_page(cursos_page)
    app.compile()
