from src.model.DAOBase import DAOBase
from src.model.POJO.Valora import Valora

class DAOValora(DAOBase):
    def agregarValoracion(self, valor):
        sql = """
        INSERT INTO cristo_media.valora
        (fecha, estrellas, comentario, idusuario, idcontenido)
        VALUES (%s, %s, %s, %s, %s)
        """

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (
                valor.getFecha(),
                valor.getEstrellas(),
                valor.getComentario(),
                valor.getUsuario().getIdUser(),
                valor.getContenido().getIdContenido()
            ))

            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha agregado correctamente la valoracion.")
            return False
        finally:
            self.cerrarCursor()

    def eliminarValoracion(self, valor):
        sql = """
        DELETE FROM cristo_media.valora
        WHERE idusuario = %s AND idcontenido = %s
        """

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (valor.id_user, valor.id_contenido))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print ("[ERROR]   No se ha eliminado correctamente la valoracion.", e)
            return False
        finally:
            self.cerrarCursor()

    """def asignarValoracionAUnUsuarioYContenido(self, valor, id_usuario, id_contenido):
        sql = 
           # INSERT INTO cristo_media.valora (fecha=%s, estrellas=%s, comentario=%s, idusuario=%s, idcontenido=%s) VALUES (%s, %s, %s, %s, %s)

        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, ())
    """