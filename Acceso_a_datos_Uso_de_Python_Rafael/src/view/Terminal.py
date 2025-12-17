from datetime import date
from src.model.POJO.Contenido import Contenido
from src.model.POJO.Usuario import Usuario
from src.controller.ControladorUsuario import ControladorUsuario
from src.controller.ControladorContenido import ControladorContenido
from src.controller.ControladorValoracion import ControladorValoracion

class Terminal:

    def __init__(self):
        self.users_controller = ControladorUsuario()
        self.contenido_controller = ControladorContenido()
        self.valoracion_controller = ControladorValoracion()
    def main(self):
        opcion = -1

        while opcion != 0:
            print("\n--- BIENVENIDO A CRISTO MEDIA ---")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("0. Salir")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                self.login_menu()
            elif opcion == 2:
                self.registrar_menu()
            elif opcion == 0:
                print("Saliendo de la aplicación...")
            else:
                print("Opción inválida")

        self.users_controller.cerrar()
        self.contenido_controller.cerrar()

    # ---------------- LOGIN ----------------
    def login_menu(self):
        username = input("User Name: ")
        password = input("Password: ")

        usuario = self.authenticate_user(username, password)

        if usuario is not None:
            print(f"¡Bienvenido {usuario.getUserName()}!")

            if usuario.getIdUser() == 2372:
                self.admin_menu()
            else:
                self.user_menu(usuario)
        else:
            print("Credenciales incorrectas.")

    # ---------------- REGISTRO ----------------
    def registrar_menu(self):
        username = input("Nombre de usuario: ")
        email = input("Email: ")

        password = ""
        password1 = ""

        while password != password1:
            password = input("Password (8-50 caracteres): ")
            password1 = input("Re-escribe la password: ")
            if password != password1:
                print("Las contraseñas no coinciden.")


        nuevo_usuario = Usuario(
            None, "inexistente", username, email, password, 0, "/home"
        )

        if self.users_controller.registrar_usuario(nuevo_usuario):
            print("Registro exitoso.")
        else:
            print("Error en el registro.")

    # ---------------- AUTENTICACIÓN ----------------
    def authenticate_user(self, name, password):
        for u in self.users_controller.get_lista_usuarios():
            if u.getUserName() == name and u.getPassword() == password:
                return u
        return None

    # ---------------- MENÚ USUARIO ----------------
    def user_menu(self, usuario):
        opcion = -1

        while opcion != 6:
            print("\n--- MENÚ USUARIO ---")
            print("0. Perfil Usuario")
            print("1. Listar mis contenidos")
            print("2. Agregar contenido")
            print("3. Actualizar contenido")
            print("4. Eliminar contenido")
            print("5. Valorar un contenido")
            print("6. Cerrar sesión")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 0:
                print(usuario)
                contenidos = self.users_controller.obtener_contenidos_por_usuario(
                    usuario.getIdUser()
                )
                for c in contenidos:
                    print(c)

            elif opcion == 1:
                contenidos = self.users_controller.obtener_contenidos_por_usuario(
                    usuario.getIdUser()
                )
                for c in contenidos:
                    print(c)

            elif opcion == 2:


                idc = int(input("ID: "))
                titulo = input("Título: ")
                ruta = input("Ruta: ")

                nuevo = Contenido(idc, titulo, ruta, 0)
                self.contenido_controller.agregar_contenido(nuevo)
                self.users_controller.asignar_contenido_a_usuario(
                    usuario.getIdUser(), nuevo.getIdContenido()
                )

            elif opcion == 5:


                idc = int(input("ID contenido: "))
                estrellas = int(input("Puntuación (1-5): "))
                comentario = input("Comentario: ")

                v = ControladorValoracion(date.today(), estrellas, comentario,
                           usuario.getIdUser(), idc)

                self.users_controller.agregar_valoracion(v)

            elif opcion == 6:
                print("Cerrando sesión...")

    def admin_menu(self):
        opcion = -1

        while opcion != 13:
            print("\n--- MENÚ ADMIN ---")
            print("1. Listar usuarios")
            print("2. Agregar usuario")
            print("3. Actualizar usuario")
            print("4. Eliminar usuario")
            print("5. Listar todos los contenidos")
            print("6. Agregar contenido")
            print("7. Actualizar contenido")
            print("8. Eliminar contenido")
            print("9. Asignar contenido a usuario")
            print("10. Ver contenidos de un usuario")
            print("11. Agregar valoración a un contenido de un usuario")
            print("12. Eliminar valoración de un contenido de un usuario")
            print("13. Cerrar sesión")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                print(self.users_controller)

            elif opcion == 2:
                self.agregar_usuario_admin()

            elif opcion == 3:
                self.actualizar_usuario_admin()

            elif opcion == 4:
                self.eliminar_usuario_admin()

            elif opcion == 5:
                print(self.contenido_controller)

            elif opcion == 6:
                self.agregar_contenido_admin()

            elif opcion == 7:
                self.actualizar_contenido_admin()

            elif opcion == 8:
                self.eliminar_contenido_admin()

            elif opcion == 9:
                self.asignar_contenido_usuario_admin()

            elif opcion == 10:
                self.ver_contenidos_usuario_admin()

            elif opcion == 11:
                id_user = int(input("ID usuario: "))
                id_contenido = int(input("ID contenido: "))
                estrellas = int(input("Puntuación (1-5): "))
                comentario = input("Comentario: ")

                v = ControladorValoracion(date.today(), estrellas, comentario, id_user, id_contenido)
                self.users_controller.agregar_valoracion_desde_usuario_a_contenido(v)

            elif opcion == 12:
                id_user = int(input("ID usuario: "))
                id_contenido = int(input("ID contenido: "))
                self.users_controller.eliminar_valoracion_de_contenido_de_usuario(
                    id_user, id_contenido
                )

            elif opcion == 13:
                print("Cerrando sesión de administrador...")

            else:
                print("Opción inválida.")

    def agregar_usuario_admin(self):
        user_name = input("Nombre de usuario: ")
        email = input("Email: ")

        password = ""
        password1 = ""
        while password != password1:
            password = input("Contraseña: ")
            password1 = input("Re-escribir contraseña: ")
            if password != password1:
                print("Las contraseñas no coinciden.")

        nuevo = Usuario(None, "activo", user_name, email, password, 0, "")
        if self.users_controller.registrar_usuario(nuevo):
            print("Usuario agregado.")
        else:
            print("Error al agregar usuario.")

    def actualizar_usuario_admin(self):
        id_user = int(input("ID del usuario a actualizar: "))
        nuevo_nombre = input("Nuevo nombre de usuario: ")
        nuevo_email = input("Nuevo email: ")
        nueva_pass = input("Nueva contraseña: ")

        usuario = Usuario(id_user, "activo", nuevo_nombre, nuevo_email, nueva_pass, 0, "")
        if self.users_controller.actualizar_usuario(usuario):
            print("Usuario actualizado.")
        else:
            print("Error al actualizar usuario.")

    def eliminar_usuario_admin(self):
        id_user = int(input("ID del usuario a eliminar: "))
        if self.users_controller.eliminar_usuario(id_user):
            print("Usuario eliminado.")
        else:
            print("Error al eliminar usuario.")

    def agregar_contenido_admin(self):
        titulo = input("Título del contenido: ")
        ruta = input("Ruta de acceso: ")

        nuevo = Contenido(None, titulo, ruta, 0)
        self.contenido_controller.agregar_contenido(nuevo)
        print("Contenido agregado.")

    def actualizar_contenido_admin(self):
        id_contenido = int(input("ID del contenido a actualizar: "))
        titulo = input("Nuevo título: ")
        ruta = input("Nueva ruta: ")

        contenido = Contenido(id_contenido, titulo, ruta, 0)
        self.contenido_controller.actualizar_contenido(contenido)
        print("Contenido actualizado.")

    def eliminar_contenido_admin(self):
        id_contenido = int(input("ID del contenido a eliminar: "))
        self.contenido_controller.eliminar_contenido(id_contenido)
        print("Contenido eliminado.")

    def asignar_contenido_usuario_admin(self):
        id_user = int(input("ID usuario: "))
        id_contenido = int(input("ID contenido: "))

        if self.users_controller.asignar_contenido_a_usuario(id_user, id_contenido):
            print("Contenido asignado al usuario.")
        else:
            print("Error al asignar contenido.")

    def ver_contenidos_usuario_admin(self):
        id_user = int(input("ID del usuario: "))
        contenidos = self.users_controller.obtener_contenidos_por_usuario(id_user)

        print("Contenidos del usuario:")
        for c in contenidos:
            print(c)

