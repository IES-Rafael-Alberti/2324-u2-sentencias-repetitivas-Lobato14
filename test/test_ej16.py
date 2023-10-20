from src.Ejercicio_16 import obtener_mayor_numero

def test_obtener_mayor_numero():
    assert obtener_mayor_numero([-1, 2, 3, 4]) == "El mayor número ingresado es: 4"
    assert obtener_mayor_numero([5, 2, 9, 1]) == "El mayor número ingresado es: 9"
    assert obtener_mayor_numero([]) == "No se ingresaron números positivos."
    assert obtener_mayor_numero([-1, -5, -9]) == "No se ingresaron números positivos."