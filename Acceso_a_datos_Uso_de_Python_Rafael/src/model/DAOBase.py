from src.model.connection.Connection import Connection

class DAOBase:
    def __init__(self):
        self.connection_obj = Connection()    
        self.conexion = self.connection_obj.getConexion()
        self.cursor = None

    def cerrarCursor(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None

    def cerrarConexionGlobal(self):
        if self.conexion is not None:
            self.conexion.close()
            self.conexion = None
