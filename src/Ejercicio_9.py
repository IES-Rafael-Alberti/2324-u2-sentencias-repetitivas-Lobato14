# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def verificar_contrasenia(contrasenia_usuario, contrasenia_correcta):
    return contrasenia_usuario == contrasenia_correcta

if __name__ == "__main__":
    # Entrada
    contrasenia_correcta = "contrasenia123"
    contrasenia_usuario = input("Introduce la contraseña: ")
    # Proceso
    if verificar_contrasenia(contrasenia_usuario, contrasenia_correcta):
        # Salida 1
        print("¡Contraseña correcta! Acceso permitido.")
    else:
        # Salida 2
        print("Contraseña incorrecta. Inténtalo de nuevo.")