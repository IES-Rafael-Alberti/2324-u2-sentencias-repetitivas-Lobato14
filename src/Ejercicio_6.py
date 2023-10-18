# Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

def tipoTriangulo(numInt):
    if not isinstance(numInt, int):
        return "Debes ingresar un número entero."
    if numInt <= 0:
        return "Debes ingresar un número entero positivo."
    triangulo = ""
    for asterisco in range(1, numInt + 1):
        triangulo += "*" * asterisco + "\n"
    return triangulo

if __name__ == "__main__":
    while True:
        try:
            numInt = int(input("Escribe un número entero positivo: "))
            if numInt <= 0:
                raise ValueError("Debes ingresar un número entero positivo.")
            resultado = tipoTriangulo(numInt)
            print(resultado)
            break
        except ValueError as error:
            print(f"Error: {error}. Intenta nuevamente.")