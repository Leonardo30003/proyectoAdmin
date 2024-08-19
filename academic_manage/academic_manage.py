import reflex as rx
from .views.login import login_page
from .views.asignacion_tareas import asignar_tarea_page
from academic_manage.views.admin.dashboard_student_horarios import create_schedule_page
from academic_manage.views.admin.dashboard_student_usuarios import register_page  
from academic_manage.views.admin.dashboard_principal import dashboard_principal_page  

# Homepage
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="./uide.png", width="80%", height="auto"),  # Replace with the actual image path
            rx.text("Sistema de registro", font_size="2.5rem", font_weight="bold", color="black"),
            rx.text("", font_size="1.2rem", color="gray"),
            rx.button("Inicia sesión", background_color="black", color="white", padding="1rem 2rem", border_radius="0.5rem", on_click=lambda: rx.redirect('/login')),
            spacing="1.5rem",
            align_items="center",
        ),
        height="100vh",
        background_color="#FFFFFF",  # Background color
    )

#==========================================PAGINA DEL DOCENTE===================

def docente() -> rx.Component:
    return rx.vstack(
        rx.box(
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(index, title="Home")  # Adding the homepag
app.add_page(
    login_page
)