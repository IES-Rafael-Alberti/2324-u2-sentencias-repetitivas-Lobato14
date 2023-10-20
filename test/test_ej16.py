from src.Ejercicio_16 import obtener_mayor_numero

def test_obtener_mayor_numero():
    lista1 = ["5", "12", "9", "7"]
    assert obtener_mayor_numero(lista1) == "El mayor número ingresado es: 12"

    lista2 = ["-5", "-12", "-9", "-7"]
    assert obtener_mayor_numero(lista2) == "Error, debe ser un número mayor a 0."

    lista3 = ["5", "-12", "9", "-7"]
    assert obtener_mayor_numero(lista3) == "Error, debe ser un número mayor a 0."

    lista4 = ["a", "b", "c"]
    assert obtener_mayor_numero(lista4) == "No se ingresaron números positivos."

    lista5 = []
    assert obtener_mayor_numero(lista5) == "No se ingresaron números positivos."