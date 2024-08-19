import reflex as rx

class Assignmsent(rx.Model, table=True):
    """Assignments for a course model"""

    anio_academico: str
    asignatura: str
    paralelo: str
    trimestre: str
    actividades_tipo: str
    actividades_asignacion: str