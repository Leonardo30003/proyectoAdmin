import reflex as rx

# Estado para manejar la navegación desde los botones
class NavState(rx.State):
    def navigate_to_users(self):
        return rx.redirect("/crear_usuarios")
    
    def navigate_to_schedule(self):
        return rx.redirect("/crear_horario")

@rx.page(
    route="/dashboard_principal",
    title="Dashboard Principal",
)
def dashboard_principal_page() -> rx.Component:
    return rx.center(
        rx.box(
            rx.heading(
                "Panel Principal",
                size="2.5em",
                color="#910048",
                text_align="center",
                margin_bottom="2em",
            ),
            rx.button(
                "Crear Usuarios",
                on_click=NavState.navigate_to_users,
                background="#001737",
                color="white",
                padding="1rem 2rem",
                border_radius="0.75em",
                box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                margin_bottom="1.5em",
                width="15em",
            ),
            rx.button(
                "Crear Horario",
                on_click=NavState.navigate_to_schedule,
                background="#001737",
                color="white",
                padding="1rem 2rem",
                border_radius="0.75em",
                box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                margin_bottom="1.5em",
                width="15em",
            ),
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content="center",
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
    app.add_page(dashboard_principal_page)
    app.compile()
