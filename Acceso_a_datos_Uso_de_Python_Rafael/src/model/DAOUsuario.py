from src.model.DAOBase import DAOBase
from src.model.POJO.Usuario import Usuario

class DAOUsuario(DAOBase):
    def agregarUsuario(self, user):
        sql = """
            INSERT INTO cristo_media.usuario
            (estado, nombreusuario, correoelectronico, contrasenia, espaciodisponible, rutausuario)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING idusuario
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (
                user.getState(),
                user.getUserName(),
                user.getEmail(),
                user.getPassword(),
                user.getSpace(),
                user.getPach()
            ))

            user.setIdUsuario(self.cursor.fetchone())
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido registrar el usuario.",e)
            return False
        finally:
            self.cerrarConexion()

    def listarUsuario(self):
        lista = []
        sql = """
            SELECT * FROM cristo_media.usuario
        """

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                lista.append(Usuario(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                ))
        finally:
            self.cerrarConexion()

        return lista

    def eliminarUsuario(self, id_usuario):
        sql = "DELETE FROM cristo_media.usuario WHERE idusuario = %s"

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (id_usuario,))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido eliminar el usuario.")
            return False
        finally:
            self.cerrarConexion()


    def asignarContenido(self, id_usuario, Contenido):
        sql = """
            INSERT INTO cristo_media.poseer (idusuario, idcontenido) VALUES (%s, %s)
        """

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (id_usuario, Contenido.getIdContenido()))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido asignar el contenido.", e)
            return False
        finally:
            self.cerrarConexion()

