from datetime import date
class Valora:

    def __init__(self, estrellas, comentario, fecha, usuario, contenido):
        self.__estrellas = estrellas
        self.__comentario = comentario
        self.__fecha = fecha
        self.__usuario = usuario
        self.__contenido = contenido

    def getEstrellas(self):
        return self.__estrellas

    def getComentario(self):
        return self.__comentario
    def getFecha(self):
        return self.__fecha
    def getUsuario(self):
        return self.__usuario
    def getContenido(self):
        return self.__contenido

    def setEstrellas(self, estrellas):
        self.__estrellas = estrellas
    def setComentario(self, comentario):
        self.__comentario = comentario
    def setFecha(self, fecha):
        self.__fecha = fecha
    def setUsuario(self, usuario):
        self.__usuario = usuario
    def setContenido(self, contenido):
        self.__contenido = contenido

    def _printValora(self):
        valorado_str = (
            f"Se han selecionado {self.__estrellas} estrellas."
            f"Se ha comentado: \n{self.__comentario}."
            f"Se ha valorado a fecha de {self.__fecha}"
            f"Se ha valorado por el usuario de id: {self.__usuario.getIdUser()} y nombre de usuario: {self.__usuario.getUserName()}"
            f"Se ha valorado el Contenido de id: {self.__contenido.getId_contenido()} y titulo de contenido: {self.__contenido.getTituloContenido()}"
        )

    def print(self):
        print(self._printValora())

    def __str__(self):
        return str(self._printValora())