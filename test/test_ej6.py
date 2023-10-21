from src.Ejercicio_6 import tipoTriangulo

def test_tipoTriangulo():
    assert tipoTriangulo(1) == "*\n"
    assert tipoTriangulo(2) == "*\n**\n"
    assert tipoTriangulo(3) == "*\n**\n***\n"
    assert tipoTriangulo(4) == "*\n**\n***\n****\n"
    assert tipoTriangulo("cadena") == "Debes ingresar un número entero."
    assert tipoTriangulo(-1) == "Debes ingresar un número entero positivo."
    assert tipoTriangulo(0) == "Debes ingresar un número entero positivo."