from src.Ejercicio_10 import es_primo

def test_es_primo():
    assert es_primo(4) == "4 no es un número primo."
    assert es_primo(5) == "5 es un número primo."
    assert es_primo(0) == "Error: Debes ingresar un número entero positivo mayor que 1."
    assert es_primo(-1) == "Error: Debes ingresar un número entero positivo mayor que 1."
    assert es_primo("hola") == "Error: Debes ingresar un número entero positivo mayor que 1."