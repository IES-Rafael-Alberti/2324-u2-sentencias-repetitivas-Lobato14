from src.Ejercicio_17 import sumaDigitos

def test_sumaDigitos():
    assert sumaDigitos(154) == "La suma de los dígitos de 154 es 10"
    assert sumaDigitos(-154) == "Error, el número debe ser un entero positivo."
    assert sumaDigitos(11) == "La suma de los dígitos de 11 es 2"
    assert sumaDigitos(0) == "Error, el número debe ser un entero positivo."
    assert sumaDigitos("hola") == "Error, el número debe ser un entero positivo."