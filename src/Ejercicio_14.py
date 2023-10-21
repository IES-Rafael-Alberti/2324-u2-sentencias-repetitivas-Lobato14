# Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números ingresados.

def sumatorioNum():
    sumatoria = 0
    salir = False
    while not salir:
        try:
            numero_usuario = input("Escribe cualquier número entero (o 0 para salir): ")
            numero = int(numero_usuario)
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")
            continue
        sumatoria += numero
        if numero == 0:
            salir = True
    
    mensaje = f"La sumatoria de los números ingresados es: {sumatoria}"
    return mensaje

if __name__ == "__main__":
    # Procesamiento y salida
    resultado = sumatorioNum()
    print(resultado)