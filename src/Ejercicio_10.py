# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es un número primo o no.

def es_primo(numero):
    if isinstance(numero, int):
        if numero <= 1:
            return "Error: Debes ingresar un número entero positivo mayor que 1."
        divisor = 2
        while divisor <= numero ** 0.5:
            if numero % divisor == 0:
                return f"{numero} no es un número primo."
            divisor += 1
        return f"{numero} es un número primo."
    else:
        return "Error: Debes ingresar un número entero positivo mayor que 1."

if __name__ == "__main__":
    numero = 0
    while numero <= 1:
        try:
            numero = int(input("Introduce un número entero positivo mayor que 1: "))
            resultado = es_primo(numero)
            print(resultado)
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Inténtalo de nuevo.")