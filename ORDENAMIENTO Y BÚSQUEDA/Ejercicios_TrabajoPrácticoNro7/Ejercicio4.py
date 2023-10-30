import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('c:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION')
# Importamos el módulo "Funciones" 
from FUNCION import Funciones

def insertion_sort_by_length(strings):
    # Recorremos la lista de cadenas desde el segundo elemento hasta el final.
    for i in range(1, len(strings)):
        # Guardamos la cadena actual en la variable current_string.
        current_string = strings[i]
        
        # Inicializamos un índice j que apunta al elemento previo al actual.
        j = i - 1
        
        # Comenzamos un bucle mientras j sea mayor o igual a 0 y la longitud de current_string
        # sea menor que la longitud de la cadena en strings[j].
        while j >= 0 and len(current_string) < len(strings[j]):
            # Movemos la cadena en strings[j] una posición hacia adelante.
            strings[j + 1] = strings[j]
            j -= 1  # Decrementamos j para comparar con el elemento previo.
        
        # Insertamos current_string en la posición correcta en la sublista ordenada.
        strings[j + 1] = current_string

# Lista de cadenas de ejemplo
strings = ["manzana", "pera", "banana", "uva", "sandía", "kiwi"]

print("Lista de cadenas sin ordenar:")
Funciones.display_list(strings)

insertion_sort_by_length(strings)

print("\nLista de cadenas ordenadas por longitud:")
Funciones.display_list(strings)