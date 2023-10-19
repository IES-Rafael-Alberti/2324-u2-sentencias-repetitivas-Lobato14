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
    numInt = 0
    while numInt <= 0:
        try:
            # Entrada
            numInt = int(input("Escribe un número entero positivo: "))
            # Proceso
            if numInt <= 0:
                # Salida 1
                print("Debes ingresar un número entero positivo.")
            else:
                # Proceso 2
                resultado = tipoTriangulo(numInt)
                # Salida 2
                print(resultado)
        except ValueError:
            # Salida 3
            print("Debes ingresar un número entero válido. Intenta nuevamente.")