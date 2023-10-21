from src.Ejercicio_19 import comprobar_opciones

def test_comprobar_opciones():
    assert comprobar_opciones(1) == "Comenzando el programa..."
    assert comprobar_opciones(2) == "Imprimiendo el listado..."
    assert comprobar_opciones(3) == "Programa finalizado. ¡Hasta luego!"
    assert comprobar_opciones(0) == "Opción no válida. Por favor, seleccione una opción del 1 al 3."
    assert comprobar_opciones(4) == "Opción no válida. Por favor, seleccione una opción del 1 al 3."
    assert comprobar_opciones(-1) == "Opción no válida. Por favor, seleccione una opción del 1 al 3."