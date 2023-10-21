# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al 
# leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo
# una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos 
# (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.

# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.

def contar_digitos_numericos(cadena):
    return sum(c.isdigit() for c in cadena)

if __name__ == "__main__":
    # Entrada
    lineas_completas = 0
    digitos_totales = 0
    linea_actual = ""
    titulo = ""
    # Procesamiento
    while titulo != "*":
        titulo = input("Libro: ")
        # Procesamiento 2
        if titulo == "/":
            digitos_en_linea = contar_digitos_numericos(linea_actual)
            # Salida 1
            print(f"Línea completa. Aparecen {digitos_en_linea} dígitos numéricos.")
            digitos_totales += digitos_en_linea
            lineas_completas += 1
            linea_actual = ""
        else:
            linea_actual += titulo
    # Salida 2
    print(f"Fin. Se leyeron {lineas_completas} líneas completas en total.")