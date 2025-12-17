import psycopg2
from configparser import ConfigParser
import os

class Connection:
    def __init__(self):
        self.driver = None
        self.protocol = None
        self.host = None
        self.port = None
        self.DBname = None
        self.user = None
        self.password = None

        self.conexion = None
        self._load_properties()
        self._connect()

    def _load_properties(self):
        config = ConfigParser()
        properties_path = os.path.join(
            os.path.dirname(__file__),
            "db.properties"
        )

        if not os.path.exists(properties_path):
            print("[ERROR]   db.properties no encontrado.")
            return

        config.read(properties_path)

        self.driver = config.get("DEFAULT", "driver", fallback="org.postgresql.Driver")
        self.protocol = config.get("DEFAULT", "protocol", fallback="jdbc:postgresql//")
        self.host = config.get("DEFAULT", "host", fallback="localhost")
        self.port = config.get("DEFAULT", "port", fallback="5432")
        self.DBname = config.get("DEFAULT", "dbname", fallback="proyecto_cristo_media")
        self.user = config.get("DEFAULT", "user", fallback="RafaelMCMLF")
        self.password = config.get("DEFAULT", "passwd", fallback="")

    def _connect(self):
        try:
            cadena = (
                f"DBname={self.DBname} " 
                f"fuser={self.user} " 
                f"password={self.password} "
                f"host={self.host} " 
                f"port={self.port}"
            )

            print("[INFO]  La cadena de conexion es: ", cadena)
            self.conexion = psycopg2.connect(cadena)
            print("[INFO]  Cadena de conexion establecia da con la base de datos PostgreSQL.")
        except psycopg2.Error as e:
            print("[ERROR]   Fallo al conectar con PostgreSQL.: \n", e)

        except Exception as e:
            print("[ERROR]   Fallo de excepcion general en: \n", e)

    def getConexion(self):
        return self.conexion

    def closeConexion(self):
        try:
            if self.conexion is not None:
                self.conexion.close()
                print("[INFO]   Conexion cerrada.")
        except psycopg2.Error as e:
            print("[ERROR]   Fallo al cerrar la conexion con PostgreSQL.: \n", e)
        except Exception as e:
            print("[ERROR]   Fallo de excepcion general en: \n", e)



