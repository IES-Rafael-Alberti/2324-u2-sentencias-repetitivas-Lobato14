from src.Ejercicio_20 import tiene_numeros, encuentraCoincidencias, encuentraPosicion

def test_tiene_numeros():
    assert tiene_numeros("Hola123") == True
    assert tiene_numeros("SoloLetras") == False

def test_encuentraCoincidencias():
    assert encuentraCoincidencias("Hello", "o") == 4
    assert encuentraCoincidencias("Hello", "a") == -1

def test_encuentraPosicion():
    assert encuentraPosicion(4, "o") == "La letra 'o' se encontró en la posición 4"
    assert encuentraPosicion(-1, "a") == "La letra 'a' no se encontró en la frase."