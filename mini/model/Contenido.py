class Contenido:

    def __init__(self, id=0, titulo="", ruta=""):
        self.__idContenido = id
        self.__tituloContenido = titulo
        self.__rutaContenido = ruta
        
    def __getContenidoId__ (self):
        return self.__idContenido
    
    def __getContenidoTitulo__ (self):
        return self.__tituloContenido
    
    def __getContenidoRuta__ (self):
        return self.__getContenidoRuta
    
    def __setContenidoId (self, i):
         self.__idContenido = i
    
    def __setContenidoTitulo (self, t):
        self.__tituloContenido = t
    
    def __setContenidoRuta(self, r):
        self.__rutaContenido = r

    def agregarContenidoAlObjeto(self, i,t,r):
        self.__setContenidoId(i)
        self.__setContenidoTitulo(t)
        self.__setContenidoRuta(r)
        
    def __str__(self):
        return f"Contenido(id={self.__idContenido}),(titulo={self.__tituloContenido}),(ruta={self.__rutaContenido}))"
    
    
def leerFicheros (data):
    try:
        with open("archivo.txt", "r", encoding="utf-8" ) as f:
            data = f.read()
            print (f"El fichero contiende: {data}")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print("La excepcion es: ", e)

def escribirFicheros ():
    
    try:
        with open("archivo.txt", "a", encoding="utf-8") as f:
            f.write("Adios\n")
            f.write("Mundo\n")
    except FileExistsError:
        print("")
    except Exception as e:
        print(f"la excepcion es: {e}")
        
if __name__ == "__main__":
    c = Contenido()
    print(c)
    c.agregarContenidoAlObjeto(2,"d","/y")
    print(c.__str__)
    
    data = ""
    leerFicheros(data)
    escribirFicheros()
    leerFicheros(data)