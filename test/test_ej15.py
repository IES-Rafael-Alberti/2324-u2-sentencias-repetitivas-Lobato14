from src.Ejercicio_15 import sumatorioNumPos
from unittest.mock import patch

@patch("builtins.input", side_effect=["5", "3", "-4", "0"])
def test_sumatorio_numeros_positivos(mock_input):
    resultado = sumatorioNumPos()
    assert resultado == "La sumatoria de los números ingresados es: 8"

@patch("builtins.input", side_effect=["-5", "0"])
def test_sumatorio_numero_negativo(mock_input):
    resultado = sumatorioNumPos()
    assert resultado == "La sumatoria de los números ingresados es: 0"

@patch("builtins.input", side_effect=["abc", "-2", "0"])
def test_sumatorio_entrada_invalida(mock_input):
    resultado = sumatorioNumPos()
    assert resultado == "La sumatoria de los números ingresados es: 0"