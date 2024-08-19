import reflex as rx

class User(rx.Model, table=True):
    "Modelo del Usuario"
    name: str
    last_name: str
    email: str
    cedula: str
    rol: str
    active: bool
