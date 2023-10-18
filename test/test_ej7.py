from src.Ejercicio_7 import tablaDeMultiplicar

def test_tablaDeMultiplicar():
    resultado_esperado = ""
    for numero in range(1, 11):
        for contador in range(1, 11):
            resultado_esperado += f"{numero} * {contador} = {numero * contador}\n"
    assert tablaDeMultiplicar() == resultado_esperado