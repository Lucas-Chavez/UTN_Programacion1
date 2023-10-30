import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('c:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION')
# Importamos el módulo "Funciones" 
from FUNCION import Funciones

# Función para ordenar una lista utilizando el algoritmo Merge Sort
def merge_sort(arr):
    # Verifica si la longitud de la lista es mayor que 1 (se puede dividir en sublistas)
    if len(arr) > 1:
        # Calcula el índice medio para dividir la lista en dos mitades
        mid = len(arr) // 2
        
        # Divide la lista en las mitades izquierda y derecha
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Realiza llamadas recursivas para ordenar las mitades izquierda y derecha
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa índices para las mitades izquierda, derecha y la lista original
        i = j = k = 0

        # Combinar las mitades izquierda y derecha en la lista original
        while i < len(left_half) and j < len(right_half):
            # Compara elementos de las mitades y coloca el menor en la lista original
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Combinar los elementos restantes (si los hay) de las mitades izquierda y derecha
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Generar una lista de números aleatorios
numbers = Funciones.create_random_list(10, 1, 100)

print("Lista de números sin ordenar:")
Funciones.display_list(numbers)

# Ordenar la lista utilizando Merge Sort
merge_sort(numbers)

print("Lista de números ordenados:")
Funciones.display_list(numbers)
