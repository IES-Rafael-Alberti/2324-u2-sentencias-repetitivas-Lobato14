# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numImpares(numPos):
    if not isinstance(numPos, int):
        return "Por favor, ingresa un número entero positivo."
    if numPos <= 0:
        return []
    impares = []
    for numero in range(1, numPos + 1, 2):
        impares.append(numero)
    return impares

if __name__ == "__main__":
    numPos = 0
    while numPos <= 0:
        try:
            numPos = int(input("Escribe un número entero positivo: "))
            if numPos <= 0:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero positivo válido.")
    
    impares = numImpares(numPos)
    if isinstance(impares, list):
        print(", ".join(map(str, impares)))
    else:
        print(impares)