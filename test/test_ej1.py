from src.Ejercicio_1 import mostrar_palabra_10_veces

def test_mostrar_palabra_10_veces():
    assert mostrar_palabra_10_veces("") == ""
    assert mostrar_palabra_10_veces(42) == "42\n42\n42\n42\n42\n42\n42\n42\n42\n42\n"
    assert mostrar_palabra_10_veces("Hola") == "Hola\nHola\nHola\nHola\nHola\nHola\nHola\nHola\nHola\nHola\n"