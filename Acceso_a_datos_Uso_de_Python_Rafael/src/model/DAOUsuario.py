from src.model.DAOBase import DAOBase
from src.model.POJO.Usuario import Usuario
from src.model.POJO.Contenido import Contenido # Importación necesaria para listar contenidos

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
                user.getStateUsuario(),
                user.getUserName(),
                user.getEmailUsuario(),
                user.getPassword(),
                user.getSpaceUsuario(),
                user.getPachUsuario()
            ))

            # Fetchone devuelve una tupla, ej: (33,)
            result = self.cursor.fetchone()
            if result:
                user.setIdUser(result[0])
                
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido registrar el usuario.", e)
            return False
        finally:
            self.cerrarCursor()

    def listarUsuario(self):
        lista = []
        sql = "SELECT idusuario, estado, nombreusuario, correoelectronico, contrasenia, espaciodisponible, rutausuario FROM cristo_media.usuario"
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                lista.append(Usuario(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                ))
        except Exception as e:
            print("[ERROR] Error al listar usuarios:", e)
        finally:
            self.cerrarCursor()
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
            self.cerrarCursor()

    # NUEVO MÉTODO: El que pedía el controlador
    def obtenerContenidosPorUsuario(self, id_usuario):
        lista = []
        sql = """
            SELECT c.idcontenido, c.nombrecontenido, c.rutacontenido, c.tamanio 
            FROM cristo_media.contenido c
            JOIN cristo_media.poseer p ON c.idcontenido = p.idcontenido
            WHERE p.idusuario = %s
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (id_usuario,))
            for row in self.cursor.fetchall():
                lista.append(Contenido(row[0], row[1], row[2], row[3]))
        except Exception as e:
            print("[ERROR] No se han podido obtener los contenidos del usuario:", e)
        finally:
            self.cerrarCursor()
        return lista

    # AJUSTADO: Aceptar id_contenido directamente como pide el controlador
    def asignarContenidoAUsuario(self, id_usuario, id_contenido):
        sql = "INSERT INTO cristo_media.poseer (idusuario, idcontenido) VALUES (%s, %s)"
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (id_usuario, id_contenido))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido asignar el contenido.", e)
            return False
        finally:
            self.cerrarCursor()
        
    def actualizarUsuario(self, user: Usuario):
        sql = """
            UPDATE cristo_media.usuario
            SET nombreusuario = %s, correoelectronico = %s, contrasenia = %s
            WHERE idusuario = %s
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (
                user.getUserName(),
                user.getEmailUsuario(),
                user.getPassword(),
                user.getIdUser()
            ))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR] No se ha podido actualizar el usuario:", e)
            return False
        finally:
            self.cerrarCursor()