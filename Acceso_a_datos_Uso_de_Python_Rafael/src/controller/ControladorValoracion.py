from src.model.DAOValora import DAOValora
from src.model.POJO.Valora import Valora

class ControladorValoracion:
    def __init__(self):
        self.dao = DAOValora()
        self.listarValoraciones = []  # lista vacía

    def getListaValoraciones(self):
        return self.listarValoraciones

    def agregarValoracionDesdeUnUsuarioAUnContenido(self, valoracion):
        self.dao.agregarValoracion(valoracion)
        self.listarValoraciones.append(valoracion)

    def eliminarValoracionDeUnContenidoDeUnUsuario(self, valoracion):
        self.dao.eliminarValoracion(valoracion)
        self.listarValoraciones = [
            v for v in self.listarValoraciones
            if not (v.usuario == valoracion.usuario and v.contenido == valoracion.contenido)
        ]
