import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('c:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION')
# Importamos el módulo "Funciones" 
from FUNCION import Funciones

def counting_sort(arr):
    # Encuentra el valor máximo en la lista
    max_value = max(arr)  # Encuentra el valor máximo en la lista para determinar el rango

    # Inicializa un arreglo de conteo con ceros
    count = [0] * (max_value + 1)  # Crea una lista de conteo con ceros para cada valor en el rango

    # Llena el arreglo de conteo
    for num in arr:
        count[num] += 1  # Incrementa el contador correspondiente al valor actual en la lista

    # Reconstruye la lista ordenada
    sorted_arr = []  # Inicializa una lista vacía para almacenar la lista ordenada
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])  # Agrega cada elemento al resultado según su frecuencia

    return sorted_arr  # Devuelve la lista ordenada utilizando el ordenamiento por conteo


# Lista de números enteros de ejemplo
numbers = Funciones.create_random_list(10, 1, 100)

print("Lista de números sin ordenar:")
Funciones.display_list(numbers)

sorted_numbers = counting_sort(numbers)

print("Lista de números ordenados:")
Funciones.display_list(sorted_numbers)