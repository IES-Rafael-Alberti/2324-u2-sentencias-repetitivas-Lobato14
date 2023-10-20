# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
# imprimir la suma de los dígitos que lo componen. La condición de corte es que se 
# ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por 
# el usuario fueron números pares.

def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

if __name__ == "__main__":
    # Entrada 1
    numeros_pares = 0
    numero = 0
    # Proceso 1
    while numero != -1:
        # Entrada 2
        numero = int(input("Ingrese un número entero positivo (-1 para salir): "))
        # Proceso 2
        if numero > 0:
            # Proceso 2
            suma = suma_digitos(numero)
            # Salida 1
            print("La suma de los dígitos es:", suma)
            # Proceso 3
            if numero % 2 == 0:
                numeros_pares += 1
        elif numero != -1:
            # Salida 2
            print("Error, el número debe ser un entero positivo.")
    # Salida 3
    print("Cantidad de números pares ingresados:", numeros_pares)