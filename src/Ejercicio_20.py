# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
# indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def tiene_numeros(frase):
    for caracter in frase:
        if caracter.isdigit():
            return True
    return False

def encuentraCoincidencias(frase, letra):
    posicion_encontrada = -1
    iteraciones = 0
    while iteraciones < len(frase) and posicion_encontrada == -1:
        if frase[iteraciones] == letra:
            posicion_encontrada = iteraciones
        iteraciones += 1
    return posicion_encontrada

def encuentraPosicion(posicion_encontrada, letra):
    if posicion_encontrada != -1:
        return f"La letra '{letra}' se encontró en la posición {posicion_encontrada}"
    else:
        return f"La letra '{letra}' no se encontró en la frase."

if __name__ == "__main__":
    # Entrada
    frase = input("Ingrese una frase: ")
    while tiene_numeros(frase):
        print("Por favor, ingrese una frase sin números.")
        frase = input("Ingrese una frase: ")
    # Entrada 2
    letra = input("Ingrese una letra: ")
    while len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingrese solo una letra.")
        letra = input("Ingrese una letra: ")
    # Proceso
    posicion_encontrada = encuentraCoincidencias(frase, letra)
    resultado = encuentraPosicion(posicion_encontrada, letra)
    # Salida
    print(resultado)