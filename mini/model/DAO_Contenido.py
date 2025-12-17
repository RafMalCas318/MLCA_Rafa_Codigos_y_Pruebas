import Contenido
import Conexion
class DAO(Conexion):
    def __init__(self):
        self.__conectado = Conexion
        self.__conten = Contenido

    def agregarContenido (self, i,t,r):
        self.__conten.Contenido.agregarContenidoAlObjeto(i,t,r)
        
    