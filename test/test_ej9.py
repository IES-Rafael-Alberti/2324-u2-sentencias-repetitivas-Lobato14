from src.Ejercicio_9 import verificar_contrasenia

def test_verificar_contrasenia():
    assert verificar_contrasenia("contrasenia123", "contrasenia123") == True
    assert verificar_contrasenia("contrasenia123", "otracontrasenia") == False
    assert verificar_contrasenia("password", "contrasenia123") == False