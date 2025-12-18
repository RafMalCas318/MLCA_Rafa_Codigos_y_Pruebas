
class Contenido:
    def __init__(self, id_contenido, nameContenido, pachContenido, sizeContenido):
        self.__id_contenido = id_contenido
        self.__nameContenido = nameContenido
        self.__pachContenido = pachContenido
        self.__sizeContenido = sizeContenido
        self.__arrayAUsuarios = []

    def getIdContenido(self):
        return self.__id_contenido

    def getNameContenido(self):
        return self.__nameContenido

    def getPachContenido(self):
        return self.__pachContenido

    def getSizeContenido(self):
        return self.__sizeContenido

    def getUsuarioContenido(self):
        return self.__arrayAUsuarios

    def setIdContenido(self, id_contenido):
        self.__id_contenido = id_contenido

    def setNameContenido(self, nameContenido):
        self.__nameContenido = nameContenido

    def setPachContenido(self, pachContenido):
        self.__pachContenido = pachContenido

    def setSizeContenido(self, sizeContenido):
        self.__sizeContenido = sizeContenido

    def setUsuarioContenido(self, u):
        self.__arrayAUsuarios.append(u)

    def _printContenido(self):
        contenido_str = (
            f"ID Contenido: {self.__id_contenido}\n"
            f"Título: {self.__nameContenido}\n"
            f"Ruta de Acceso: {self.__pachContenido}\n"
            f"Tamaño: {self.__sizeContenido}\n"
        )
        return contenido_str

    def print(self):
        print(self._printContenido())

    def __str__(self):
        return self._printContenido()

