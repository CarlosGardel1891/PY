from Persona import Persona

# Crear una lista vacía de personas
lista_Personas = []
# Crear una lista vacía de Casas
lista_Casas = []

def menu():
    print("1- Ingresar una persona")
    print("2- Ingresar una casa")
    print("3- Cambiar propietario de casa")
    print("4- Asignar casa a persona")
    print("5- Asignar persona a casa")
    print("6- Ingrese la opcion que desea ejecutar")
    print("7- Salir")
    opcion = int(input("Ingrese la opcion que desea realizar"))
    return opcion
resultado = menu()