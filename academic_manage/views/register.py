import reflex as rx
from datetime import datetime
from ..backend.backend_register import State

class FormState(rx.State):
    name: str = ""
    last_name: str = ""
    email: str = ""
    cedula: str = ""
    rol: str = "Docente"
    active: bool = True

    def handle_change(self, key: str, value: str):
        setattr(self, key, value)

    def handle_checkbox(self, value: bool):
        self.active = value

    def handle_register(self):
        user_data = {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "cedula": self.cedula,
            "rol": self.rol,
            "active": self.active,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        result = State.add_user_to_db(user_data)
        if result:
            print("Usuario creado exitosamente")
            rx.window_alert("Usuario registrado exitosamente.")
            return rx.redirect("/login")
        else:
            self.handle_existing_user()

    def handle_existing_user(self):
        print("El usuario ya existe. Redirigiendo a la página de login.")
        rx.window_alert("El usuario ya existe. Serás redirigido a la página de inicio de sesión.")
        return rx.redirect("/login")

def signup_form() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/uide.png",
                        width="12em",
                        height="auto",
                        border_radius="50px",
                        border="5px solid #555"
                    ),
                    rx.heading(
                        "Registro de Usuario",
                        size="2.5em",
                        color="#FF011D",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%"
                ),
                rx.vstack(
                    rx.text(
                        "Nombre",
                        size="1.5em",
                        color="#001737",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Nombre",
                        on_change=lambda value: FormState.handle_change("name", value),
                        style={
                            "width": "100%",
                            "border_color": "#001737",
                            "background_color": "#F8F8F8",
                            "color": "#001737",
                            "border": "1px solid #001737",
                            "border_radius": "0.65em",
                            "padding": "0.50em",
                        },
                    ),
                    rx.text(
                        "Apellido",
                        size="1.5em",
                        color="#001737",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Apellido",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",
                        background_color="#F8F8F8",
                        color="#001737",
                        border="1px solid #001737",
                        border_radius="0.75em",
                        padding="0.50em",
                        on_change=lambda value: FormState.handle_change("last_name", value),
                    ),
                    rx.text(
                        "Correo Electrónico",
                        size="1.5em",
                        color="#001737",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="ejemplo@gmail.com",
                        type="email",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",
                        background_color="#F8F8F8",
                        color="#001737",
                        border="1px solid #001737",
                        border_radius="0.75em",
                        padding="0.50em",
                        on_change=lambda value: FormState.handle_change("email", value),
                    ),
                    rx.text(
                        "Cédula",
                        size="1.5em",
                        color="#001737",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Cédula",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",
                        background_color="#F8F8F8",
                        color="#001737",
                        border="1px solid #001737",
                        border_radius="0.75em",
                        padding="0.50em",
                        on_change=lambda value: FormState.handle_change("cedula", value),
                    ),
                    rx.text(
                        "Rol",
                        size="1.5em",
                        color="#001737",
                        text_align="left",
                        width="100%",
                    ),
                    rx.select(
                        ["Docente", "Administrador"],
                        placeholder="Seleccione un rol",
                        color_scheme="blue",
                        size="3",
                        on_change=lambda value: FormState.handle_change("rol", value),
                    ),
                    rx.box(
                        rx.checkbox(
                            rx.text("Activo", color="black"),
                            default_checked=FormState.active,
                            on_change=lambda value: FormState.handle_checkbox(value),
                            color_scheme="indigo",
                        ),
                    ),
                    rx.button(
                        "Registrarse",
                        size="1.5em",
                        width="100%",
                        background="#001737",
                        color="white",
                        border_radius="0.75em",
                        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                        on_click=FormState.handle_existing_user,
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("¿Ya tienes una cuenta?", color="#000000"),
                    rx.link(
                        "Iniciar sesión",
                        href="/login",
                        color="#FF011D",
                        text_decoration="underline",
                        hover_color="#001737",
                    ),
                ),
                spacing="2",
                width="100%",
            ),
            size="14",
            max_width="50rem",
            width="100%",
            background_color="white",
            padding="2.5em",
            border_radius="1.5em",
            box_shadow="0 8px 10px rgba(0, 0, 0, 0.8)",
        ),
        height="100vh",
        background_color="#F0F0F0",
    )

@rx.page(route="/register", title="Registro")
def register_page() -> rx.Component:
    return signup_form()
