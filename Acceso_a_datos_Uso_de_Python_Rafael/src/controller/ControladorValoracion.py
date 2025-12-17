from src.model.DAOValora import DAOValora
from src.model.POJO.Valora import Valora
from src.model.POJO.Contenido import Contenido
from src.model.POJO.Usuario import Usuario

class ControladorValoracion:
    def __init__(self):
        self.dao = DAOValora()
        self.listarValoraciones = Valora()

    def getListaValoraciones(self):
        return self.listarValoraciones

    def agregarValoracionDesdeUnUsuarioAUnContenido(self, Valoracion):
        self.dao.agregarValoracion(Valoracion)

    def eliminarValoracionDeUnContenidoDeUnUsuario(self, Valoracion):
        self.dao.eliminarValoracion(Valoracion)