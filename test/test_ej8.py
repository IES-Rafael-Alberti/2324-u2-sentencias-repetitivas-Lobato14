from src.Ejercicio_8 import triangulo_rectangulo

def test_triangulo_rectangulo():
    assert triangulo_rectangulo(1) == "1 \n"
    assert triangulo_rectangulo(3) == "1 \n3 1 \n"
    assert triangulo_rectangulo(5) == "1 \n3 1 \n5 3 1 \n"
    assert triangulo_rectangulo(7) == "1 \n3 1 \n5 3 1 \n7 5 3 1 \n"
    assert triangulo_rectangulo(0) == "Debes ingresar un número entero positivo."
    assert triangulo_rectangulo(-1) == "Debes ingresar un número entero positivo."
    assert triangulo_rectangulo("hola") == "Debes ingresar un número entero positivo."