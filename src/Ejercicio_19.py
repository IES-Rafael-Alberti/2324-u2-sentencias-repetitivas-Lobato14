# Mostrar un menú con tres opciones: 
    # 1- comenzar programa
    # 2- imprimir listado, 
    # 3- finalizar programa.

# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
# Si elige una opción incorrecta, informarle del error. 

# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 

# Si elige las opciones 1 ó 2 se imprimirá un texto. 
# Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def mostrar_menu():
    return """
------- Menú -------
1. Comenzar programa
2. Imprimir listado
3. Finalizar programa
----------------------
"""

def comprobar_opciones(opciones_elegir):
    if opciones_elegir == 1:
        return "Comenzando el programa..."
    elif opciones_elegir == 2:
        return "Imprimiendo el listado..."
    elif opciones_elegir == 3:
        return "Programa finalizado. ¡Hasta luego!"
    else:
        return "Opción no válida. Por favor, seleccione una opción del 1 al 3."

if __name__ == "__main__":
    # Entrada
    opciones_elegir = 0
    # Proceso
    while opciones_elegir != 3:
        # Salida 1
        print(mostrar_menu())
        # Entrada 2
        entrada_user = input("Seleccione una de las opciones anteriores: ")
        # Proceso 2
        if entrada_user.isdigit():
            opciones_elegir = int(entrada_user)
            # Salida 2
            print(comprobar_opciones(opciones_elegir))
        else:
            # Salida 3
            print("Por favor, ingrese un número válido.")