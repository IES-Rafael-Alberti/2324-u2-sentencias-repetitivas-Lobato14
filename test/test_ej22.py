import pytest
from src.Ejercicio_22 import leer_numeros

@pytest.mark.parametrize("inputs, expected", [
    (["12345", "2468642", "0"], (2, 1, 9, 3)),  # Números positivos
    (["-123", "abc", "xyz", "0"], (0, 0, 0, 0)),  # Números negativos y letras
    (["0"], (0, 0, 0, 0)),  # Caso sin números
])
def test_leer_numeros(monkeypatch, inputs, expected):
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    numeros_pares, numeros_impares, digitos_pares, digitos_impares = leer_numeros()
    assert (numeros_pares, numeros_impares, digitos_pares, digitos_impares) == expected