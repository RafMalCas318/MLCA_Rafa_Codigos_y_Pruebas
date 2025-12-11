class Objeto1 :
    name = ""
    edad = 0
    def __init__ (self, nameIN, edadIN):
        self.name = nameIN
        self.edad = edadIN
    
    def getDatos (self):
        print(f"El nombre es: {self.name}")
        print(f"La edad es: {self.edad}")

arrayObjeto = []


def agregarObjeto (e):
    arrayObjeto.append(e)

def sacarObjeto ():
    for obj in arrayObjeto: 
       obj.getDatos()
        

def main ():
    v = [["Juan Carlos", 22], ["Rafael", 21], ["Alvaro", 27]]
    for persona in v : 
        nombre = persona[0]
        edad = persona[1]
        e = Objeto1(nombre,edad)
        agregarObjeto(e)
        
    sacarObjeto()
if __name__ == '__main__':
    main()