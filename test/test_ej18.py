from src.Ejercicio_18 import suma_digitos

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(456) == 15
    assert suma_digitos(789) == 24
    assert suma_digitos(0) == 0
    assert suma_digitos(1) == 1
    assert suma_digitos(11) == 2
    assert suma_digitos(111) == 3
    assert suma_digitos(123456789) == 45