#declaracion de Imports
from Persona import Persona
#declaracion de variables
out_while = 0
# Crear una lista de personas
lista_Personas = []
# Crear una lista de Casas
lista_Casas = []

def menu():
    print("1- Ingresar una persona")
    print("2- Ingresar una casa")
    print("3- Cambiar propietario de casa")
    print("4- Asignar casa a persona")
    print("5- Asignar persona a casa")
    print("6- Ingrese la opcion que desea ejecutar")
    print("7- Salir")
    opcion = input("Ingrese la opcion que desea realizar")
    return opcion

def verificar_eleccion(eleccion):
    try:
        num_value = int(eleccion)
        return True
    except ValueError:
        print("Ingrese un dato NUMERICO entre 1 y 7")
        return False

def opcion1():
    print("1")

def opcion2():
    print("2")

def opcion3():
    print("3")

def opcion4():
    print("4")

def opcion5():
    print("5")

def opcion6():
    print("6")


#-----------------------------------Main---------------------------------------------------

while out_while == 0:
    eleccion = menu()
    print(eleccion)
    if verificar_eleccion(eleccion):
        if eleccion == 1:
            opcion1()
        elif eleccion == 2:
            opcion2()
        elif eleccion == 3:
            opcion3()
        elif eleccion == 4:
            opcion4()
        elif eleccion == 5:
            opcion5()
        elif eleccion == 6:
            opcion6()
        elif eleccion == 7:
            print("Cerrando programa...")
            break
        else:
            print("Ingrese un valor entre 1 y 7")