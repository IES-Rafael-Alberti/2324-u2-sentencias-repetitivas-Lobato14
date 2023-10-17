# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad).

def aniosCumplidos(edad):
    for contador in range(1, edad + 1):
        print(contador)

if __name__ == "__main__":
    edad = input("Escriba su edad: ")
    while not edad.isdigit() or int(edad) <= 0:  
        print("Edad no válida. Intente nuevamente.")
        edad = input("Escriba su edad: ")
    edad = int(edad)
    aniosCumplidos(edad)