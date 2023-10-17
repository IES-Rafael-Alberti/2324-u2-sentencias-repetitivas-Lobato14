from src.Ejercicio_3 import numImpares

def test_numImpares():
    assert numImpares(6) == [1, 3, 5]
    assert numImpares(1) == [1]
    assert numImpares(0) == []  
    assert numImpares(-3) == []
    assert numImpares("") == "Por favor, ingresa un número entero positivo."