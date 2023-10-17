from src.Ejercicio_2 import aniosCumplidos

def test_aniosCumplidos():
    assert aniosCumplidos(6) == "1\n2\n3\n4\n5\n6"
    assert aniosCumplidos("6") == "Edad no válida. Intente nuevamente."
    assert aniosCumplidos(-4) == "Edad no válida. Intente nuevamente."
    assert aniosCumplidos(0) == "Edad no válida. Intente nuevamente."
    assert aniosCumplidos("fg") == "Edad no válida. Intente nuevamente."