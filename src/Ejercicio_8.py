# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

def triangulo_rectangulo(numEnt):
    if not isinstance(numEnt, int) or numEnt <= 0:
        return "Debes ingresar un número entero positivo."
    
    resultado = ""
    for numero in range(1, numEnt + 1, 2):
        for numero2 in range(numero, 0, -2):
            resultado += f"{numero2} "
        resultado += "\n"
    return resultado

if __name__ == "__main__":
    while True:
        try:
            numEnt = int(input("Escribe un número entero mayor que 0: "))
            if numEnt <= 0:
                raise ValueError("Debes ingresar un número entero positivo.")
            print(triangulo_rectangulo(numEnt))
            break
        except ValueError as error:
            print(f"Error: {error}. Intenta nuevamente.")