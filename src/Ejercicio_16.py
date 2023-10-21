# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
# Informar cuál fue el mayor número ingresado.

def obtener_mayor_numero(listaNumeros: list) -> str:
    numeros_positivos = [numero for numero in listaNumeros if numero > 0]
    if numeros_positivos:
        maximoNumero = max(numeros_positivos)
        return "El mayor número ingresado es: " + str(maximoNumero)
    else:
        return "No se ingresaron números positivos."

if __name__ == "__main__":
    # Entrada
    listaNumeros = []
    numeroIntPos = input("Escribe un número entero positivo (o 0 para salir): ")
    # Procesamiento
    while numeroIntPos != "0":
        if numeroIntPos.isdigit():
            numero = int(numeroIntPos)
            if numero > 0:
                listaNumeros.append(numero)
            else:
                print("Error, debe ser un número mayor a 0.")
        else:
            print("Error, debes ingresar un número entero.")
        numeroIntPos = input("Escribe un número entero positivo (o 0 para salir): ")
    resultado = obtener_mayor_numero(listaNumeros)
    # Salida
    print(resultado)