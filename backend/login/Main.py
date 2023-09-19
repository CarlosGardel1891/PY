from Usuario import Usuario
from Sistema import usuarios, agregar_usuario, devuelte_False_si_usuario_repetido, devuelte_False_si_contrasena_leve, devuelte_True_si_usuario_y_contrasena_correctos




def mostrar_Menu():
    print("Ingrese el numero de la opcion que desea realizar")
    
    print("1 Agregra usuario")
    print("2 Ingresar a usuario")
    print("3 Mostrar usuarios")
    print("4 Salir")


def agregar_Usuario():
    nombre_usuario = input("Ingrese nombre de usuario")
    contrasena = input("ingrese contraseña del usuario")
    if devuelte_False_si_usuario_repetido(nombre_usuario):
        if devuelte_False_si_contrasena_leve(contrasena):
            agregar_usuario(Usuario(nombre_usuario, contrasena, 0))
            print("Se regitro correctamente el usuario")
        else:
            print("contraseña poco segura intente ingresar otra (minimo 6 caracteres y un numero)")
    else:
        print("Nombre de usuario ya usado, no se pudo agregar usuario")


def ingresar_A_Usuario():
    nombre_usuario = input("Ingrese nombre del usuario")
    contrasena = input("ingrese contraseña del usuario")

    if devuelte_True_si_usuario_y_contrasena_correctos(nombre_usuario, contrasena):
        print(f"Se ingreso correctamente con el usuario {nombre_usuario}")
    else:
        print("no hay usuarios ingresados con los datos dados")



def imprimir_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print("Nombre de usuario:", usuario.nombre_usuario)
        print("Contraseña:", usuario.contrasena)
        print()  # Separador entre usuarios


def salir():
    exit()

menu = {
    1: agregar_Usuario,
    2: ingresar_A_Usuario,
    3: imprimir_usuarios,
    4: salir
}

while True:
        mostrar_Menu()
        opcion = input("Seleccione una opción: ")

        try:
            opcion = int(opcion)
            if opcion in menu:
                menu[opcion]()
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Ingrese UN NUMERO. Inténtelo de nuevo.")






