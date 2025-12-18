from src.model.DAOContenido import DAOContenido
from src.model.POJO.Contenido import Contenido

class ControladorContenido:
    def __init__(self):
        self.dao = DAOContenido()
        self.listarContenido = []  # lista vacía

    def getListaContenido(self):
        return self.listarContenido

    def agregarContenido(self, contenido):
        self.dao.agregarContenido(contenido)
        self.listarContenido.append(contenido)

    def actualizarContenido(self, contenido):
        if self.dao.actualizarContenido(contenido):
            self.listarContenido = [
                c if c.getIdContenido() != contenido.getIdContenido() else contenido
                for c in self.listarContenido
            ]
            return True
        return False

    def eliminarContenido(self, contenido):
        if self.dao.eliminarContenido(contenido):
            self.listarContenido = [
                c for c in self.listarContenido
                if c.getIdContenido() != contenido.getIdContenido()
            ]
            return True
        return False

    def cerrar(self):
        self.dao.cerrarConexionGlobal()
