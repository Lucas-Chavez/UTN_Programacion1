import random

def apply_function_to_list(func, input_list):
    result_list = []  # Inicializamos una lista vacía para almacenar los resultados
    for item in input_list:
        result = func(item)  # Aplicamos la función dada a cada elemento de la lista
        result_list.append(result)  # Agregamos el resultado a la lista de resultados
    return result_list  # Devolvemos la lista de resultados

# Ejemplo de uso:
def square(x):
    return x ** 2  # Una función que calcula el cuadrado de un número

# Generar una lista de números aleatorios en el rango del 1 al 10
random_numbers = random.sample(range(1, 11), 10)
squared_numbers = apply_function_to_list(square, random_numbers)

print(f"Lista sin modificar {random_numbers}")
print(f"Lista modificada {squared_numbers}")  