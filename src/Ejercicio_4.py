# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero 
# separados por comas.

def contar_atras(numPos):
    numPos = str(numPos)
    resultado = ""
    while not numPos.isdigit() or int(numPos) <= 0:
        print("Por favor, ingresa un número entero positivo.")
        numPos = input("Escribe un número entero positivo: ")
    numPos = int(numPos)
    for numero in range(numPos, -1, -1):
        resultado += str(numero)
        if numero != 0:
            resultado += ", "
    print(resultado)

if __name__ == "__main__":
    numPos = input("Escribe un número entero positivo: ")
    contar_atras(numPos)