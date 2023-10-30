import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('c:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION')
# Importamos el módulo "Funciones" 
from FUNCION import Funciones

def bubble_sort(arr):
    n = len(arr)  # Obtenemos la longitud de la lista
    for i in range(n - 1):
        # Establecemos una bandera para verificar si se realizó algún intercambio en esta pasada
        swapped = False
        
        # Iteramos a través de la lista hasta el penúltimo elemento
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Indicamos que se realizó un intercambio
        
        # Si no se realizó ningún intercambio en esta pasada, la lista ya está ordenada
        if not swapped:
            break

my_list = Funciones.create_random_list(10, 1, 100)
print("Lista sin ordenar sus elementos:")
Funciones.display_list(my_list)

bubble_sort(my_list)
print("Lista con sus elementos ordenados:")
Funciones.display_list(my_list)
