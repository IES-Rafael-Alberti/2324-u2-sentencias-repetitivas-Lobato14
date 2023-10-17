# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def mostrar_palabra_10_veces(palabra):
    numero = 10
    while numero > 0:
        print(palabra)
        numero = numero - 1

if __name__=="__main__":
    palabra = input("Escribe una palabra: ")
    mostrar_palabra_10_veces(palabra)