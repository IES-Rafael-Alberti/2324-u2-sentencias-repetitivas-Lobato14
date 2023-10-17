import sys
import io
from src.Ejercicio_1 import mostrar_palabra_10_veces

def test_mostrar_palabra_10_veces(capsys, monkeypatch):
    palabra = "Juan"
    monkeypatch.setattr(sys, "stdin", io.StringIO(palabra + "\n"))

    # Capturamos la salida estándar
    with capsys.disabled():
        salida = mostrar_palabra_10_veces(palabra)
        # Imprime la salida para verificación manual
        print(salida)  

    output_lines = salida.strip().split("\n")

    # Verificamos que la salida contiene la palabra repetida 10 veces
    assert len(output_lines) == 10
    assert all(line == palabra for line in output_lines)