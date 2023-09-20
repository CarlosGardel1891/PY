from Usuario import Usuario

# Lista de usuarios
usuarios = []
# Variable encargada de llevar los numeros de usuarios
num_usuario = 0

# Encargada de agragr los usuarios a las listas
def agregar_usuario(usuario):
    usuarios.append(usuario)

#antes de agregar corobora que no esten nombres repetidos
def devuelte_False_si_usuario_repetido(nombre_usuario):
    for usuario in usuarios:
        if nombre_usuario == usuario.nombre_usuario:
            return False
    
    return True

#verifica antes de agregar que la contraseña sea fuerte
def devuelte_False_si_contrasena_leve(contrasena):
    cantidad_caracteres = len(contrasena)
    cantidad_numeros = 0
    for caracter in contrasena:
        if caracter.isdigit():
            cantidad_numeros += 1
    
    if cantidad_caracteres > 6 and cantidad_numeros > 0:
        return True
    else:
        return False

#para ingresa a un usuario esta es la funcion que valida nombre y contraseña
def devuelte_True_si_usuario_y_contrasena_correctos(nombre, contrasena):
    for usuario in usuarios:
        if nombre == usuario.nombre_usuario and contrasena == usuario.contrasena:
            return True
    
    return False

# encargada de asignarle el numero de usuario
def numero_usuario():
    global num_usuario 
    num_usuario = num_usuario + 1
    return (num_usuario -1)

    