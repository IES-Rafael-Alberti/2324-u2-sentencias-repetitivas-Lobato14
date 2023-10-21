# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).

def aniosCumplidos(edad):
    # Con isinstance verificamos que sea un número entero positivo.
    if not isinstance(edad, int) or edad <= 0:
        return "Edad no válida. Intente nuevamente."
    numeros = ""
    for contador in range(1, edad + 1):
        numeros += str(contador) + "\n"
    return numeros.strip()  # Con strip eliminamos caracteres especiales

if __name__ == "__main__":
    # Entrada
    edad = input("Escriba su edad: ")
    # Proceso
    while not edad.isdigit() or int(edad) <= 0:  
        print("Edad no válida. Intente nuevamente.")
        edad = input("Escriba su edad: ")
    edad = int(edad)
    resultado = aniosCumplidos(edad)
    # Salida
    print(resultado)