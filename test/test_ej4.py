from src.Ejercicio_4 import contar_atras

def test_contar_atras_numero_positivo():
    assert contar_atras(5) == "5, 4, 3, 2, 1, 0"
    # assert contar_atras("Hola") == "Escribe un número entero positivo: "
    assert contar_atras(0) == "0"