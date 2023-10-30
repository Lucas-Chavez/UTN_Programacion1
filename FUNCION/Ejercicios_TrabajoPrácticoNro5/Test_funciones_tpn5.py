import pytest
from Ejercicio13 import calcular_modulo_vector
from Ejercicio14 import is_prime_number
from Ejercicio10 import apply_discount

@pytest.mark.parametrize("a, b, res", [
    (80, 75, 109.66),  # Especifica el resultado con 2 decimales
    (50, 150, 158.11)  # Especifica el resultado con 2 decimales
])
def test_calcular_modulo_vector(a, b, res):
    assert calcular_modulo_vector(a, b) == res


@pytest.mark.parametrize("a, res", [
    (827, True),  
    (977, True),  
    (996, False)
])
def test_is_prime_number(a, res):
    assert is_prime_number(a) == res


@pytest.mark.parametrize("a, b, res", [
    ({"producto1": 100,"producto2": 50,"producto3": 75}, {"producto1": 10,"producto3": 15}, 203.75)
])
def test_apply_discount(a, b, res):
    assert apply_discount(a, b) == res