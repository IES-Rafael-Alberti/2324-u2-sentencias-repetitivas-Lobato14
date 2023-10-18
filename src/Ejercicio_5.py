# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

def calcular_inversion(cantidadInv, interesAnual, numAnios):
    if cantidadInv < 0 or interesAnual < 0 or numAnios < 0:
        return "Por favor, ingresa valores no negativos."
    
    resultados = []
    for anio in range(1, numAnios + 1):
        cantidadAnual = cantidadInv * (1 + interesAnual / 100) ** anio
        resultados.append(("En el año", anio, "la cantidad ha sido de", round(cantidadAnual, 2)))
    return resultados

if __name__ == "__main__":
    cantidadInv = float(input("Escribe la cantidad a invertir: "))
    interesAnual = float(input("Escribe el interés anual en porcentaje: "))
    numAnios = int(input("Escribe el número de años: "))
    resultados = calcular_inversion(cantidadInv, interesAnual, numAnios)
    for resultado in resultados:
        print(" ".join(str(elemento) for elemento in resultado))