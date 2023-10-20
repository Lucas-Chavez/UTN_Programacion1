import pytest
import sys

# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('C:/Users/chave/OneDrive/Escritorio/GIT-PROGRAMACION/FUNCION')

# Importamos el módulo "Funciones" que contiene las funciones que queremos probar.
import Funciones

@pytest.mark.parametrize("a, res", [
    (123, 6),  # Prueba con el número 123, cuya suma de dígitos es 6.
    (5, 5)  # Prueba con el número 375, cuya suma de dígitos es 15.
])
def test_add_digits(a, res):
    # Comprobamos si la función "add_digits" retorna el resultado esperado (res) para el valor de entrada (a).
    assert Funciones.add_digits(a) == res

@pytest.mark.parametrize("a, res", [
    ([1, 2, 3], 6),  # Prueba con una lista [1, 2, 3], cuya suma es 6.
    ([3, 7, 5], 15)  # Prueba con una lista [3, 7, 5], cuya suma es 15.
])
def test_addition_number(a, res):
    # Comprobamos si la función "addition_number" retorna el resultado esperado (res) para la lista de entrada (a).
    assert Funciones.addition_number(a) == res