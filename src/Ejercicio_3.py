# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numImpares(numPos):
    impares = []
    for numero in range(1, numPos + 1, 2):
        impares.append(numero)
    return impares

if __name__ == "__main__":
    numPos = int(input("Escribe un número entero positivo: "))
    if numPos <= 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        impares = numImpares(numPos)
        print(", ".join(map(str, impares)))