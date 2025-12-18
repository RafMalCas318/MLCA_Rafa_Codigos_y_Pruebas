from src.model.DAOBase import DAOBase
from src.model.POJO.Contenido import Contenido


class DAOContenido(DAOBase):
    def agregarContenido(self, contenido):
        sql = """
            INSERT INTO cristo_media.contenido (nombrecontenido, rutacontenido, tamanio) VALUES (%s, %s, %s)
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (
                contenido.getNombrecontenido(),
                contenido.getRutacontenido(),
                contenido.getTamaniocontenido()
            ))
            contenido.setIdContenido(self.cursor.fetchone())
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha podido agregar el contenido: ", e)
            return False
        finally:
            self.cerrarCursor()

    def listarContenidos(self):
        lista = []
        sql = """
            SELECT * FROM cristo_media.contenido
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                lista.append(Contenido(
                    row[0], row[1], row[2], row[3]
                ))
        finally:
            self.cerrar

        return lista

    def eliminarContenido(self, idContenido):
        sql = """
            DELETE FROM cristo_media.contenido WHERE idcontenido = %s
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (idContenido,))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha eliminado el contenido: ", e)
            return False
        finally:
            self.cerrarCursor()

    def actualizarContenido(self, contenido):
        sql = """
            UPDATE cristo_media.contenido SET nombrecontenido=%s, rutacontenido=%s, tamanio=%s WHERE idcontenido=%s
        """
        try:
            self.cursor = self.conexion.cursor()
            self.cursor.execute(sql, (contenido.getIdContenido()))
            self.conexion.commit()
            return True
        except Exception as e:
            self.conexion.rollback()
            print("[ERROR]   No se ha actualizado el contenido: ", e)
            return False
        finally:
            self.cerrarCursor()


