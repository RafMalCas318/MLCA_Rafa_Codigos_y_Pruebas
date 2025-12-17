from src.model.connection.Connection import Connection

class DAOBase(Connection):
    def __init__(self):
        conexion = Connection()
        self.conexion = Connection.getConexion()
        self.cursor = None

    def cerrarConexion(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None

    def cerrarConexionGlobal(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None