# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero)):
        if numero % i == 0:
            return False
    return True
   
if __name__ == "__main__":
    # Entrada
    numeros_primos = 0
    intentos_maximos = 100  
    continuar = True
    # Proceso
    try:
        while intentos_maximos > 0 and continuar:
            numero = int(input("Ingrese un número (0 para salir y solo números mayores que 1): "))
            if es_primo(numero):
                numeros_primos += 1
            else:
                # Salida 1
                print("Por favor, ingrese un número primo mayor que 1.")
            intentos_maximos -= 1
        # Salida 2
        print(f"Se ingresaron {numeros_primos} números primos.")
    except ValueError:
        raise ValueError("Error")