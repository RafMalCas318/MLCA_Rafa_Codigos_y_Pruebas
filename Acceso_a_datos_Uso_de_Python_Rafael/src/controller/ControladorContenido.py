from src.model.DAOContenido import DAOContenido
from src.model.POJO.Contenido import Contenido
from src.model.POJO.Usuario import Usuario
from src.model.POJO.Valora import Valora

class ControladorContenido:
    def __init__(self):
        self.dao = DAOContenido()
        self.listarContenido = Contenido()

    def getListaContenido(self):
        return self.listarContenido

    def agregarContenido(self, contenido):
        self.dao.agregarContenido(contenido)

    def actualizarContenido(self, contenido):
        if self.dao.actualizarContenido(contenido) == True:
            self.listarContenido.append(contenido)
            return True
        return False

    def eliminarContenido(self, contenido):
        if self.dao.eliminarContenido(contenido) == True:
            self.listarContenido = [
                c for c in self.listarContenido
                    if c.getIdContenido() != contenido.getIdContenido()

            ]
            return True
        return False

    def cerrar(self):
        self.dao.cerrarConexion()
