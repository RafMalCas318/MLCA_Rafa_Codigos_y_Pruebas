
class Usuario:
    def __init__(self, id_user, stateUsuario, userName, emailUsuario, password, spaceUsuario, pachUsuario):
        self.__id_user = id_user
        self.__stateUsuario = stateUsuario
        self.__userName = userName
        self.__emailUsuario = emailUsuario
        self.__password = password
        self.__spaceUsuario = spaceUsuario
        self.__pachUsuario = pachUsuario
        self.__arrayAContenido = []

    def getIdUser(self):
        return self.__id_user

    def getStateUsuario(self):
        return self.__stateUsuario

    def getUserName(self):
        return self.__userName

    def getEmailUsuario(self):
        return self.__emailUsuario

    def getPassword(self):
        return self.__password

    def getSpaceUsuario(self):
        return self.__spaceUsuario

    def getPachUsuario(self):
        return self.__pachUsuario

    def getArrayAContenido(self):
        return self.__arrayAContenido

    def setIdUser(self, id_user):
        self.__id_user = id_user

    def setStateUsuario(self, stateUsuario):
        self.__stateUsuario = stateUsuario

    def setUserName(self, userName):
        self.__userName = userName

    def setEmailUsuario(self, emailUsuario):
        self.__emailUsuario = emailUsuario

    def setPassword(self, password):
        self.__password = password

    def setSpaceUsuario(self, spaceUsuario):
        self.__spaceUsuario = spaceUsuario

    def setPachUsuario(self, pachUsuario):
        self.__pachUsuario = pachUsuario

    def setArrayAContenido(self, arrayAContenido):
        self.__arrayAContenido = arrayAContenido

    def _printUsuario(self):
        usuario_str = (
            f"ID Usuario: {self.__id_user}\n"
            f"Nombre Usuario: {self.__userName}\n"
            f"Email Usuario: {self.__emailUsuario}\n"
            f"Password Usuario: {self.__password}\n"
            f"Espacio Usuario: {self.__spaceUsuario}\n"
            f"Estado Usuario: {self.__stateUsuario}\n"
            f"Ruta Usuario: {self.__pachUsuario}\n"
        )
        return usuario_str

    def print(self):
        print(self._printUsuario())

    def __str__(self):
        return self._printUsuario()