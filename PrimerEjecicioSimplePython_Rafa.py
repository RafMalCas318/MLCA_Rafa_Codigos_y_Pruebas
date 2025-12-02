def Pregunta1():
    print("-----------------------------------------------------")
    print("1. ¿De dónde viene el nombre de este lenguaje de programacion?")
    print("a) De Los Monty Python")
    print("b) De La Serpiente De Nombre Pitón")

    respuesta = input("Introduce una respuesta (a/b): ").lower() 

    if respuesta == "a":
        return True
    elif respuesta == "b":
        return False
    else:
        print("La respuesta dada no entra dentro de las permitidas.")
        return False

def Pregunta2():
    print("-----------------------------------------------------")
    print("2. ¿Que tipo de lenguaje de programación es Python?")
    print("a) Compilado")
    print("b) Interpretado")
    print("c) Compilado e Interpretado")
    print("d) Seminterpretado")
    
    respuesta = input("Introduce una respuesta (a/b/c/d): ").lower()

    if respuesta == "b":
        return True
    else:
        if respuesta not in ('a', 'b', 'c', 'd'):
            print("La respuesta dada no entra dentro de las permitidas.")
        return False 

def Pregunta3():
    print("-----------------------------------------------------")
    print("3. ¿Cómo se debe comentar dentro de un fichero .py?")
    print("a) // Esto es un comentario")
    print("b) # Esto es un comentario")
    print("c) /* Esto es un comentario */")
    print("d) -- Esto es un comentario")

    respuesta = input("Introduce una respuesta (a/b/c/d): ").lower()
    
    if respuesta == "b":
        return True
    else:
        if respuesta not in ('a', 'b', 'c', 'd'):
            print("La respuesta dada no entra dentro de las permitidas.")
        return False

def Pregunta4():
    print("--------------------------------------------------------")
    print("4. ¿Cómo se ejecuta un fichero .py?")
    print("a) pt fichero.py")
    print("b) python fichero")
    print("c) run fichero.py")
    print("d) python fichero.py")
    
    respuesta = input("Introduce una respuesta (a/b/c/d): ").lower()
    if respuesta == "d":
        return True
    else:
        if respuesta not in ('a', 'b', 'c', 'd'):
            print("La respuesta dada no entra dentro de las permitidas.")
        return False


def Controler():
    puntuacion = 0
    preguntas = [Pregunta1, Pregunta2, Pregunta3, Pregunta4]
    
    print("-------------------------------------------------------")
    print("-- Cuestionario del lenguaje de programación Python. --")
    print("-------------------------------------------------------")

    for i, pregunta_func in enumerate(preguntas):
        
        if pregunta_func():
            puntuacion += 1
            print("¡Respuesta Correcta! ✅")
        else:
            print("Respuesta Incorrecta. ❌")

        input("\nPulsa Enter para continuar...") 
        print("\n")
        
    print("--------------------------------------------------------------------------")
    print(f"----- Has completado el cuestionario. Tu puntuación es: {puntuacion}/4 -----")
    print("--------------------------------------------------------------------------")

if __name__ == "__main__":
    Controler()