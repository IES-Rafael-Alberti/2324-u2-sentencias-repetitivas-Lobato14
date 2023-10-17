from src.Ejercicio_4 import contar_atras

def test_contar_atras():
    assert contar_atras(0) == "Por favor, ingresa un número entero positivo."
    assert contar_atras(-1) == "Por favor, ingresa un número entero positivo."
    assert contar_atras("") == "Por favor, ingresa un número entero positivo."
    assert contar_atras(4) == "4, 3, 2, 1, 0"