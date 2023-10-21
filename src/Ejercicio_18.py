# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
# imprimir la suma de los dígitos que lo componen. La condición de corte es que se 
# ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por 
# el usuario fueron números pares.

def suma_digitos(numero):
    try:
        numero = int(numero)
        if numero < 0:
            return "Error, el número debe ser un entero positivo."
        return sum(int(digito) for digito in str(numero))
    except ValueError:
        return "Error, por favor ingrese un número entero válido."

def contar_numeros_pares(numeros):
    count = 0
    for numero in numeros:
        if numero < 0:
            return "Error, el número debe ser un entero positivo."
        if numero % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    numeros_pares = 0
    numeros_ingresados = []
    numero_str = input("Ingrese un número entero positivo (-1 para salir): ")
    while numero_str != "-1":
        if numero_str.isdigit():
            suma = suma_digitos(numero_str)
            print("La suma de los dígitos es:", suma)
            if isinstance(suma, int):
                numero = int(numero_str)
                numeros_ingresados.append(numero)
                if numero % 2 == 0:
                    numeros_pares += 1
            else:
                print(suma)
        else:
            print("Error, por favor ingrese un número entero válido.")
        numero_str = input("Ingrese un número entero positivo (-1 para salir): ")
    print("Cantidad de números pares ingresados:", contar_numeros_pares(numeros_ingresados))