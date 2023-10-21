import pytest
from src.Ejercicio_24 import es_primo

@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (4, False),
        (5, True),
        (7, True),
        (-4, False)
    ],
)

def test_contar_digitos_numericos(inputs, expected_output):
    assert es_primo(inputs) == expected_output