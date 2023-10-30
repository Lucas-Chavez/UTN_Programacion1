import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('c:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION')
# Importamos el módulo "Funciones" 
from FUNCION import Funciones

def find_largest_element(lst):
    # Si la lista está vacía, retornamos None ya que no hay elementos para comparar.
    if len(lst) == 0:
        return None

    # Si la lista tiene un solo elemento, ese elemento es el más grande, así que lo retornamos.
    if len(lst) == 1:
        return lst[0]

    # Dividimos la lista en dos mitades.
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    # Llamamos recursivamente la función en ambas mitades para encontrar el máximo en cada una.
    max_left = find_largest_element(left)
    max_right = find_largest_element(right)

    # Comparamos los máximos encontrados en las dos mitades y retornamos el máximo global.
    return max(max_left, max_right)


my_list = Funciones.create_random_list(10, 1, 100)
print("Elementos de la lista:")
Funciones.display_list(my_list)

largest = find_largest_element(my_list)
print("El elemento más grande en la lista es:", largest)




