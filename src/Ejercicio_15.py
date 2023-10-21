# Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def sumatorioNumPos():
    sumatoria = 0
    salir = False
    while not salir:
        try:
            numero_usuario = input("Escribe cualquier número entero (o 0 para salir): ")
            numero = int(numero_usuario)
        except ValueError:
            print("Entrada inválida. Introduce un número entero positivo.")
            continue

        if numero < 0:
            print("No se pueden introducir números negativos. Introduce un número entero positivo.")
        else:
            sumatoria += numero

        if numero == 0:
            salir = True
    
    mensaje = f"La sumatoria de los números ingresados es: {sumatoria}"
    return mensaje

if __name__ == "__main__":
    # Procesamiento
    resultado = sumatorioNumPos()
    # Salida
    print(resultado)