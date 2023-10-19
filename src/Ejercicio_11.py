# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.

def palabraReves(palabra):
    while not (palabra and palabra.isalpha()):
        palabra = input("Por favor, escribe una palabra: ")
    palabra_invertida = ""
    for letra in range(len(palabra) - 1, -1, -1):
        palabra_invertida += palabra[letra]
    return "Palabra invertida: " + palabra_invertida

if __name__ == "__main__":
    # Entrada
    palabra = input("Escribe una palabra: ")
    # Proceso
    palabra_invertida = palabraReves(palabra)
    # Salida
    print(palabra_invertida)