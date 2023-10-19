from src.Ejercicio_12 import vecesLetra
from src.Ejercicio_12 import es_palabra_valida

def test_es_palabra_valida():
    assert es_palabra_valida("Hola mundo") == True
    assert es_palabra_valida("123") == False
    assert es_palabra_valida("UnaPalabra") == False

def test_vecesLetra():
    assert vecesLetra("Hola mundo", "o") == "La letra o aparece 2 veces en la frase 'Hola mundo'."
    assert vecesLetra("Python es genial", "a") == "La letra a aparece 1 veces en la frase 'Python es genial'."
    assert vecesLetra("Esto es una prueba", "z") == "La letra z aparece 0 veces en la frase 'Esto es una prueba'."