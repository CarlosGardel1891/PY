from Usuario import Usuario


usuarios = []

def agregar_usuario(usuario):
    usuarios.append(usuario)

def devuelte_False_si_usuario_repetido(nombre_usuario):
    print("entro")
    for usuario in usuarios:
        if nombre_usuario == usuario.nombre_usuario:
            return False
    
    return True

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