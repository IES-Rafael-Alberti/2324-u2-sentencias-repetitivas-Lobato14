# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def mostrar_palabra_10_veces(palabra):
    numero = 10
    salida = ""
    while numero > 0:
        salida += palabra + "\n"
        numero -= 1
    return salida