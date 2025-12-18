from src.model.DAOUsuario import DAOUsuario
from src.model.POJO.Usuario import Usuario
from src.model.POJO.Contenido import Contenido
from src.model.POJO.Valora import Valora

class ControladorUsuario:
    def __init__(self):
        self.dao = DAOUsuario()
        self.listarUsuarios = self.dao.listarUsuario()

    def getListaUsuarios(self):
        return self.listarUsuarios
    def agregarUsuario(self, usuario):
        if self.dao.agregarUsuario(usuario) == True:
            self.listarUsuarios.append(usuario)
            return True
        return False

    def actualizarUsuario(self, usuario):
        if self.dao.actualizarUsuario(usuario) == True:
            self.listarUsuarios.append(usuario)
            return True
        return False

    def eliminarUsuario(self, usuario):
        if self.dao.eliminarUsuario(usuario) == True:
            self.listarUsuarios = [
                u for u in self.listarUsuarios
                    if u.getIdUser() != usuario.getIdUser()
            ]
            return True
        return False

    def asignarContenidoAUsuario(self, id_usuario, id_contenido):
        return self.dao.asignarContenidoAUsuario(id_usuario, id_contenido)

    def obtenerContenidosPorUsuario(self, id_usuario):
        return self.dao.obtenerContenidosPorUsuario(id_usuario)

    def cerrar(self):
        self.dao.cerrarConexionGlobal()

    def agregarValoracionDesdeUsuarioAUnContenido(self, Valora):
        self.dao.agregarValoracionDesdeUsuario(Valora)

    def eliminarValoracionDeUnContenidoDeUnUsuario(self, id_usuario, contenido):
        self.eliminarValoracionDeUnContenidoDeUnUsuario(id_usuario, contenido)

    def obtenerValoracionesdeContenidosDeUsuario(self, id_usuario):
        return self.dao.obtenerValoracionesdeUsuario(id_usuario)

