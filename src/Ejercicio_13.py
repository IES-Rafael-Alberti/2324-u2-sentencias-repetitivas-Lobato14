# Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba "salir" que terminará.

def ecoUsuario(palabraclave):
    palabraTecl = input("Escribe lo que quieras: ")
    while palabraTecl != palabraclave:
        palabraTecl = input("Escribe lo que quieras: ")
    return "Saliendo del programa...."

if __name__ == "__main__":
    # Entrada
    palabraclave = "salir"
    # Proceso
    mensaje = ecoUsuario(palabraclave)
    # Salida
    print(mensaje)