from src.Ejercicio_18 import suma_digitos, contar_numeros_pares

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(-456) == "Error, el número debe ser un entero positivo."
    assert suma_digitos("4-56") == "Error, por favor ingrese un número entero válido."
    assert suma_digitos("48-6") == "Error, por favor ingrese un número entero válido."

def test_contar_numeros_pares():
    assert contar_numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert contar_numeros_pares([1, -3, 5, 7, 9]) == "Error, el número debe ser un entero positivo."