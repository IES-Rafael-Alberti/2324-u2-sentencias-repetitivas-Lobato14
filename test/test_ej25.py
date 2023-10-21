from src.Ejercicio_25 import encontrar_palabra_mas_larga, contar_numero_palabras

def test_palabra_mas_larga():
    palabra_mas_larga = encontrar_palabra_mas_larga("Natalia tiene una botella")
    assert palabra_mas_larga == "Natalia"

def test_contar_numero_palabras():
    palabra_mas_larga = contar_numero_palabras("Natalia tiene una botella")
    assert palabra_mas_larga == 4