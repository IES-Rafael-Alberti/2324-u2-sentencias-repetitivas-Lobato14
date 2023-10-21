# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más 
# de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al 
# carácter “ “ (espacio), ya sea uno o más.

def encontrar_palabra_mas_larga(frase):
    palabras = frase.split(" ")

    longitud_palabra_mas_larga = 0
    palabra_mas_larga = ""

    for palabra in palabras:
        if len(palabra) > longitud_palabra_mas_larga:
            longitud_palabra_mas_larga = len(palabra)
            palabra_mas_larga = palabra
    return palabra_mas_larga

def contar_numero_palabras(frase):
    palabras = frase.split(" ")
    return len(palabras)

if __name__ == "__main__":
    entrada_valida = False
    while not entrada_valida:
        # Entrada
        frase = input("Por favor, ingrese una frase: ")
        # Verificar si la frase contiene números
        for char in frase:
            if (char.isdigit()):
                print("Error: La frase no puede contener números. Intente de nuevo.")
            else:
                palabra_mas_larga = encontrar_palabra_mas_larga(frase)
                entrada_valida = True
    print("La palabra más larga es:", palabra_mas_larga)
    print("Cantidad de palabras en la frase:", contar_numero_palabras(frase))