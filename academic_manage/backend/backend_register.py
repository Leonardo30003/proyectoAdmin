import reflex as rx
from datetime import datetime
from sqlmodel import select
from ..models.user_model import User

class State(rx.State):
    """El estado de la app."""

    users: list[User] = []
    current_user: User = User()

    def load_users(self):
        """Cargar todos los usuarios desde la base de datos."""
        try:
            with rx.session() as session:
                self.users = session.exec(select(User)).all()
        except Exception as e:
            rx.window_alert(f"Error al cargar usuarios: {str(e)}")

    @staticmethod
    def add_user_to_db(form_data: dict) -> bool:
        """Agregar un usuario a la base de datos."""
        form_data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with rx.session() as session:
                existing_user = session.exec(
                    select(User).where(User.email == form_data["email"])
                ).first()
                if existing_user:
                    rx.window_alert("El usuario con este correo ya existe.")
                    return False  # Usuario ya existe

                session.add(User(**form_data))
                session.commit()
                State().load_users()  # Actualizar la lista de usuarios después de agregar uno nuevo
                return True  # Registro exitoso
        except Exception as e:
            rx.window_alert(f"Error al agregar usuario: {str(e)}")
            return False

    def update_user_to_db(self, form_data: dict) -> None:
        """Actualizar un usuario en la base de datos."""
        try:
            with rx.session() as session:
                user = session.exec(
                    select(User).where(User.id == form_data["id"])
                ).first()
                if not user:
                    rx.window_alert("Usuario no encontrado.")
                    return

                for field, value in form_data.items():
                    if field != "id":
                        setattr(user, field, value)
                
                session.add(user)
                session.commit()
                self.load_users()
                rx.toast.info(f"Usuario {form_data['name']} ha sido modificado.", variant="outline", position="bottom-right")
        except Exception as e:
            rx.window_alert(f"Error al actualizar usuario: {str(e)}")

    def delete_user(self, id: int) -> None:
        """Eliminar un usuario de la base de datos."""
        try:
            with rx.session() as session:
                user = session.exec(select(User).where(User.id == id)).first()
                if not user:
                    rx.window_alert("Usuario no encontrado.")
                    return

                session.delete(user)
                session.commit()
                self.load_users()
                rx.toast.info(f"Usuario {user.name} ha sido eliminado.", variant="outline", position="bottom-right")
        except Exception as e:
            rx.window_alert(f"Error al eliminar usuario: {str(e)}")

# Asegúrate de que en el archivo 'register.py' estés usando la instancia correcta de State
# y que esté correctamente inicializada y accesible donde se usa `handle_register`.
