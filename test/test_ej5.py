from src.Ejercicio_5 import calcular_inversion

def test_calcular_inversion():
    resultados = calcular_inversion(1000, 10, 3)
    assert resultados == [
        ("En el año", 1, "la cantidad ha sido de", 1100.0),
        ("En el año", 2, "la cantidad ha sido de", 1210.0),
        ("En el año", 3, "la cantidad ha sido de", 1331.0)
    ]

    resultado_invalido = calcular_inversion(-1000, 10, 3)
    assert resultado_invalido == "Por favor, ingresa valores no negativos."

    resultado_invalido = calcular_inversion(1000, -10, 3)
    assert resultado_invalido == "Por favor, ingresa valores no negativos."

    resultado_invalido = calcular_inversion(1000, 10, -3)
    assert resultado_invalido == "Por favor, ingresa valores no negativos."