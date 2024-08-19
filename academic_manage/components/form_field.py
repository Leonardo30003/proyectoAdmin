import reflex as rx


import reflex as rx

def form_field(label, placeholder, input_type, field_name, icon):
    return rx.hstack(
        rx.icon("layout-dashboard", size=16, stroke_width=1.5),  # Cambié 'columns' a 'layout-dashboard'
        rx.input(
            placeholder=placeholder,
            type=input_type,
            name=field_name,
        ),
        rx.text(label),
    )
