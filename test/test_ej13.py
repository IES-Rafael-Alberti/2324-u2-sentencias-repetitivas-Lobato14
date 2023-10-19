# Importa la clase `patch` del módulo unittest.mock para simular la entrada del usuario.
from unittest.mock import patch
from src.Ejercicio_13 import ecoUsuario

def test_ecoUsuario():
    # Utiliza el contexto `patch` para simular la entrada del usuario.
    with patch('builtins.input', side_effect=["14", "-1", "Hola", "Salir"]):
        # Llama a la función `ecoUsuario` con la palabra clave "Salir".
        # Las respuestas simuladas son "14", "-1", "Hola" y "Salir".
        # La función debe salir del bucle y devolver "Saliendo del programa....".
        assert ecoUsuario("Salir") == "Saliendo del programa...."