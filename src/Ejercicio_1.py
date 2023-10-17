# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def mostrar_palabra_10_veces(palabra):
    palabra = str(palabra)
    if palabra:
        numero = 10
        salida = ""
        while numero > 0:
            salida += palabra + "\n"
            numero -= 1
        return salida
    else:
        return ""
    
if __name__ == "__main__":
    palabra = input("Escribe una palabra o número: ")
    resultado = mostrar_palabra_10_veces(palabra)
    print(resultado)