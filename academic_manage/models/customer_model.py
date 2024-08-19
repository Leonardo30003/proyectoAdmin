import reflex as rx 

class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
    date: str
    payments: float
    status: str