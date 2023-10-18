# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es un número primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    divisor = 2
    while divisor <= numero ** 0.5:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Introduce un número entero positivo mayor que 1: "))
            if numero <= 1:
                print("Error: Debes ingresar un número entero positivo mayor que 1.")
            else:
                if es_primo(numero):
                    print(numero, "es un número primo.")
                else:
                    print(numero, "no es un número primo.")
                break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Inténtalo de nuevo.")