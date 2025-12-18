import psycopg2
from configparser import ConfigParser
import os

class Connection:
    def __init__(self):
        self.host = None
        self.port = None
        self.dbname = None
        self.user = None
        self.password = None
        self.schema = None
        self.conexion = None

        self._load_properties()
        self._connect()

    def _load_properties(self):
        config = ConfigParser()
        properties_path = os.path.join(os.path.dirname(__file__), "db.properties")

        if not os.path.exists(properties_path):
            print("[ERROR] db.properties no encontrado.")
            return

        config.read(properties_path)
        db = config["database"]

        self.host = db.get("host", "localhost")
        self.port = int(db.get("port", 5432))
        self.dbname = db.get("dbname", "proyecto_cristo_media")
        self.user = db.get("user", "")
        self.password = db.get("password", "")
        self.schema = db.get("schema", "")

    def _connect(self):
        try:
            self.conexion = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print(f"[INFO] Conexión establecida con la base de datos '{self.dbname}' en {self.host}:{self.port}")
        except psycopg2.Error as e:
            print("[ERROR] Fallo al conectar con PostgreSQL:\n", e)
        except Exception as e:
            print("[ERROR] Fallo de excepción general:\n", e)

    def getConexion(self):
        return self.conexion

    def closeConexion(self):
        if self.conexion:
            try:
                self.conexion.close()
                print("[INFO] Conexión cerrada.")
            except Exception as e:
                print("[ERROR] Fallo al cerrar la conexión:\n", e)
