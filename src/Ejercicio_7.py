# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablaDeMultiplicar():
    tabla = ""
    for numero in range(1, 11):
        for contador in range(1, 11):
            resultado = numero * contador
            tabla += f"{numero} * {contador} = {resultado}\n"
    return tabla

if __name__ == "__main__":
    print(tablaDeMultiplicar())