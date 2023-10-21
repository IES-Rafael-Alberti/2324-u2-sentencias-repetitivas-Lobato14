import pytest
from src.Ejercicio_23 import contar_digitos_numericos


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        ("Los 3 mosqueteros", 1),
        ("Historia de 2 ciudades", 1),
        ("20000 leguas de viaje submarino", 5),
    ],
)

def test_contar_digitos_numericos(inputs, expected_output):
    assert contar_digitos_numericos(inputs) == expected_output