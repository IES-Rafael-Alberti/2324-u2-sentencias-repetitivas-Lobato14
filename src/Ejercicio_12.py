# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

def es_palabra_valida(frase):
    return len(frase.split()) > 1 and not any(c.isdigit() for c in frase)

def vecesLetra(frase, letra):
    contador = 0
    for veces in frase:
        if veces == letra:
            contador += 1
    return "La letra " + letra + " aparece " + str(contador) + " veces en la frase '" + frase + "'."

if __name__ == "__main__":
    # Entrada
    frase = input("Introduce una frase: ")

    while not es_palabra_valida(frase):
        print("La frase debe contener más de una palabra y no puede contener números.")
        frase = input("Introduce una frase válida: ")

    letra = input("Introduce una letra: ")

    while len(letra) != 1:
        print("Por favor, introduce solo una letra.")
        letra = input("Introduce una letra: ")

    resultado = vecesLetra(frase, letra)
    # Salida
    print(resultado)