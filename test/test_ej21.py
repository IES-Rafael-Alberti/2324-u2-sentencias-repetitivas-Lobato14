from src.Ejercicio_21 import totalMonto

def test_totalMonto_sin_descuento():
    compras = [500, 300, 200]
    assert totalMonto(compras) == 1000

def test_totalMonto_con_descuento():
    compras = [600, 500, 400]
    assert totalMonto(compras) == 1350  # 1500 - 150 (10% de descuento)

def test_totalMonto_sin_compras():
    compras = []
    assert totalMonto(compras) == 0

def test_totalMonto_con_compras_negativas():
    compras = [150, 20, -5]
    assert totalMonto(compras) == 170

def test_totalMonto_con_una_compra_negativa():
    compras = [-200]
    assert totalMonto(compras) == 0

def test_totalMonto_con_descuento_menor_a_1000():
    compras = [200, 300, 400]
    assert totalMonto(compras) == 900