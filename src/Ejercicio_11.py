# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.

def palabraReves(palabra):
    while palabra == "":
        palabra = input("Por favor, escribe una palabra: ")
    for letra in range(len(palabra) - 1, -1, -1):
        print(palabra[letra])
    return palabra

if __name__ == "__main__":
    # Entrada
    palabra = input("Escribe una palabra: ")
    # Proceso
    resultado = palabraReves(palabra)
    # Salida
    print(resultado)