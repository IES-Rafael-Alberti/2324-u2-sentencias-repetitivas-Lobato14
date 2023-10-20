# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos 
# que lo componen.

def sumaDigitos(numPositivo):
    numPositivo_str = str(numPositivo)
    if numPositivo_str.isdigit():
        numPositivo_int = int(numPositivo_str)
        if numPositivo_int > 0:
            suma_digitos = sum(int(digito) for digito in numPositivo_str)
            return "La suma de los dígitos de " + numPositivo_str + " es " + str(suma_digitos)
        else:
            return "Error, el número debe ser un entero positivo."
    else:
        return "Error, el número debe ser un entero positivo."

if __name__ == "__main__":
    # Entrada
    numPositivo = input("Escribe un número entero positivo: ")
    # Proceso
    while not numPositivo.isdigit() or int(numPositivo) <= 0:
        print("Error, el número debe ser un entero positivo.")
        numPositivo = input("Escribe un número entero positivo: ")
    resultado = sumaDigitos(int(numPositivo))
    # Salida
    print(resultado)