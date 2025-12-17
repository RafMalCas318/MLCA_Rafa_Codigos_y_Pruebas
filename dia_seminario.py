#Ejemplos Simples:
tupla = (1, 2, 3, 'cuatro')
biblio = {1 : "Hola", 2: " ", 3 : "mundo", 4 : "!"}

def tuplaEjemplo1 ():
    print(f"es tuplaEjemplo1: ", tupla)

def tuplaEjemplo2 ():
    l = list(tupla)
    print(f"Es tuplaEjemplo2: ", l)

def diccionarioEjemplo1 ():
    print(f"le diccionario saca: ",biblio[1],biblio[2],biblio[3],biblio[4])

def diccionarioEjemplo2 ():
    print(f"le diccionario saca entero: ",biblio)
    
    
def bluclesForIn ():
    for d in tupla:
        print(f"Es :", d)

'''def bublesForInt2 ():
    for i in range[5]:
        print("La i vale: ", i)'''


def ejemplosSimples ():
    tuplaEjemplo1 ()
    tuplaEjemplo2 ()
    diccionarioEjemplo1 ()
    diccionarioEjemplo2 ()
    bluclesForIn ()
    #bublesForInt2 ()
    print(f" ")

#Objeto1:
class usuario:
    id = 0
    nombre = ""
    passwd = ""
    def __init__ (self, nombre, passwd):
        self.id = 1
        self.nombre = nombre
        self.passwd = passwd
        
    def getUsuario (self):
        print(f"El nombre de usuario es: ", self.nombre)
        print(f"La contraseña es: ", self.passwd)
    
def main2 ():
    print ("Objeto 1 usuario: ")
    nombre = ""
    contra = ""
    nombre = input("Introduce el nombre: ").lower() 
    contra = input("Introduce la contraseña: ").lower() 
    u = usuario(nombre, contra)
    u.getUsuario()
    print (" ")

#objeto con herencia 1:
class so:
    tipo = ""
    def __init__(self, tipo):
        self.tipo = tipo
    
    def get (self):
        print("El tipo de sistema opertivo es: ", self.tipo)
class pc:
    peso = 0
    def __init__(self, peso):
        self.peso = peso
    
    def get (self):
        print("El peso del pc es de: ", self.peso)

class portatil(pc, so):
    def __init__(self, peso, tipo):
        pc.__init__(self, peso)
        so.__init__(self, tipo)
    
    def get (self):
        print("El peso del portatil es: ", self.peso)
        print("El sistema operativo es: ", self.tipo)

def main3 ():
    d = portatil(22, "windows")
    d.get()   
    print(" ")
if __name__ == "__main__":
    ejemplosSimples ()
    main2 ()
    main3 ()