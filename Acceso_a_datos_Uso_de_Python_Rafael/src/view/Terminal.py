from datetime import date
from src.model.POJO.Contenido import Contenido
from src.model.POJO.Usuario import Usuario
from src.model.POJO.Valora import Valora
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

            try:
                opcion = int(input("Selecciona una opción: "))
            except ValueError:
                continue

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

        if usuario:
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
        password1 = "1"

        while password != password1:
            password = input("Password: ")
            password1 = input("Re-escribe la password: ")
            if password != password1:
                print("Las contraseñas no coinciden.")

        nuevo_usuario = Usuario(None, "activo", username, email, password, 0, "/home")
        
        if self.users_controller.agregarUsuario(nuevo_usuario):
            print("Registro exitoso.")
        else:
            print("Error en el registro.")

    def authenticate_user(self, name, password):
        for u in self.users_controller.getListaUsuarios():
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
            print("5. Valorar un contenido")
            print("6. Cerrar sesión")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 0:
                print(usuario)
            elif opcion == 1:
                contenidos = self.users_controller.obtenerContenidosPorUsuario(usuario.getIdUser())
                for c in contenidos:
                    print(c)
            elif opcion == 2:
                titulo = input("Título: ")
                ruta = input("Ruta: ")
                nuevo = Contenido(None, titulo, ruta, 0)
                self.contenido_controller.agregarContenido(nuevo)
                self.users_controller.asignarContenidoAUsuario(usuario.getIdUser(), nuevo.getIdContenido())
            elif opcion == 5:
                idc = int(input("ID contenido: "))
                estrellas = int(input("Puntuación (1-5): "))
                comentario = input("Comentario: ")

                # Buscar objeto Contenido por ID
                contenido_obj = next(
                    (c for c in self.contenido_controller.getListaContenido() if c.getIdContenido() == idc),
                    None
                )
                if not contenido_obj:
                    print("Contenido no encontrado")
                    continue

                # Crear valoración correctamente
                v = Valora(estrellas, comentario, date.today(), usuario, contenido_obj)
                self.valoracion_controller.agregarValoracionDesdeUnUsuarioAUnContenido(v)
            elif opcion == 6:
                print("Cerrando sesión...")

    # ---------------- MENÚ ADMIN ----------------
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
            print("8. Eliminar contenido")
            print("11. Agregar valoración")
            print("12. Eliminar valoración")
            print("13. Cerrar sesión")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                for u in self.users_controller.getListaUsuarios(): print(u)
            elif opcion == 2:
                self.agregar_usuario_admin()
            elif opcion == 3:
                self.actualizar_usuario_admin()
            elif opcion == 4:
                id_u = int(input("ID a eliminar: "))
                u_eliminar = Usuario(id_u, None, None, None, None, 0, None)
                self.users_controller.eliminarUsuario(u_eliminar)
            elif opcion == 5:
                for c in self.contenido_controller.getListaContenido(): print(c)
            elif opcion == 6:
                self.agregar_contenido_admin()
            elif opcion == 8:
                id_c = int(input("ID contenido a eliminar: "))
                c_eliminar = Contenido(id_c, None, None, 0)
                self.contenido_controller.eliminarContenido(c_eliminar)
            elif opcion == 11:
                id_u = int(input("ID usuario: "))
                id_c = int(input("ID contenido: "))
                usuario_obj = next(
                    (u for u in self.users_controller.getListaUsuarios() if u.getIdUser() == id_u),
                    None
                )
                contenido_obj = next(
                    (c for c in self.contenido_controller.getListaContenido() if c.getIdContenido() == id_c),
                    None
                )
                if not usuario_obj or not contenido_obj:
                    print("Usuario o contenido no encontrado")
                    continue
                estrellas = int(input("Puntos: "))
                comentario = input("Comentario: ")
                v = Valora(estrellas, comentario, date.today(), usuario_obj, contenido_obj)
                self.valoracion_controller.agregarValoracionDesdeUnUsuarioAUnContenido(v)
            elif opcion == 12:
                id_u = int(input("ID usuario: "))
                id_c = int(input("ID contenido: "))
                usuario_obj = next(
                    (u for u in self.users_controller.getListaUsuarios() if u.getIdUser() == id_u),
                    None
                )
                contenido_obj = next(
                    (c for c in self.contenido_controller.getListaContenido() if c.getIdContenido() == id_c),
                    None
                )
                if not usuario_obj or not contenido_obj:
                    print("Usuario o contenido no encontrado")
                    continue
                v_eliminar = Valora(None, None, None, usuario_obj, contenido_obj)
                self.valoracion_controller.eliminarValoracionDeUnContenidoDeUnUsuario(v_eliminar)
            elif opcion == 13:
                print("Cerrando sesión admin...")

    def agregar_usuario_admin(self):
        u = Usuario(None, "activo", input("User: "), input("Email: "), input("Pass: "), 0, "")
        self.users_controller.agregarUsuario(u)

    def actualizar_usuario_admin(self):
        u = Usuario(int(input("ID: ")), "activo", input("User: "), input("Email: "), input("Pass: "), 0, "")
        self.users_controller.actualizarUsuario(u)

    def agregar_contenido_admin(self):
        c = Contenido(None, input("Título: "), input("Ruta: "), 0)
        self.contenido_controller.agregarContenido(c)

if __name__ == "__main__":
    app = Terminal()
    app.main()
