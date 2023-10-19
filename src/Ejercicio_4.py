# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero 
# separados por comas.

def contar_atras(numPos):
    numPos = str(numPos)
    while not numPos.isdigit() or int(numPos) <= 0:
        numPos = input("Escribe un número entero positivo: ")
    numPos = int(numPos)
    resultado = ""
    for numero in range(numPos, -1, -1):
        resultado += str(numero)
        if numero != 0:
            resultado += ", "
    return resultado

if __name__ == "__main__":
    # Entrada
    numPos = input("Escribe un número entero positivo: ")
    # Salida
    print(contar_atras(numPos))