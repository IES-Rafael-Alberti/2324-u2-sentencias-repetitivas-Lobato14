# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
# Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad 
# de dígitos pares y de dígitos impares leídos en total.

def contar_digitos_pares_impares(numero):
    pares = 0
    impares = 0
    
    for digito in str(numero):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

def leer_numeros():
    numeros_pares = 0
    numeros_impares = 0
    digitos_pares = 0
    digitos_impares = 0
    
    numero = input("Ingrese un número entero positivo (0 para terminar): ")
    
    while numero != '0':
        if numero.isdigit() and int(numero) >= 0:
            pares, impares = contar_digitos_pares_impares(int(numero))
            
            digitos_pares += pares
            digitos_impares += impares
            
            numeros_pares += 1 if pares > 0 else 0
            numeros_impares += 1 if impares > 0 else 0
        else:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")
        
        numero = input("Ingrese un número entero positivo (0 para terminar): ")
    
    return numeros_pares, numeros_impares, digitos_pares, digitos_impares

if __name__ == "__main__":
    # Entrada y Proceso
    numeros_pares, numeros_impares, digitos_pares, digitos_impares = leer_numeros()
    # Salida
    print("Cantidad total de números pares leídos:", numeros_pares)
    print("Cantidad total de números impares leídos:", numeros_impares)
    print("Cantidad total de dígitos pares leídos:", digitos_pares)
    print("Cantidad total de dígitos impares leídos:", digitos_impares)