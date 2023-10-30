# Definir una función para ingresar números en una lista
def input_numbers():
    numbers_list = []
    while True:
        try:
            number = int(input("Ingrese un número (0 para finalizar): "))  # Solicita un número al usuario
            if number == 0:  # Si el número ingresado es 0, termina el bucle
                break
            else:
                numbers_list.append(number)  # Agrega el número a la lista
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Maneja excepciones de tipo ValueError
    return numbers_list  # Devuelve la lista de números ingresados

# Definir una función para eliminar un número de la lista
def remove_number(numbers_list, number_to_remove):
    if number_to_remove in numbers_list:
        numbers_list.remove(number_to_remove)  # Si el número está en la lista, elimina la primera ocurrencia
        print(f"Se ha eliminado la primera ocurrencia de {number_to_remove}.")
    else:
        print(f"El número {number_to_remove} no se encuentra en la lista y no se puede eliminar.")

def calculate_frequencies(list_number):
    # Inicializar una lista vacía para almacenar las frecuencias de los elementos
    frequency_list = []
    # Iterar a través de los elementos de la lista de números
    for element in list_number:
        # Verificar si ya hemos procesado un elemento similar en la lista de frecuencias
        if not any(item[0] == element for item in frequency_list):
            # Contar cuántas veces aparece el elemento en la lista original
            count = list_number.count(element)
            # Agregar una tupla con el elemento y su frecuencia a la lista de frecuencias
            frequency_list.append((element, count))
    # Crear una cadena con las tuplas formateadas
    frequency_items = ", ".join(f"({element}, {count})" for element, count in frequency_list)

    # Devolver la cadena con las frecuencias formateadas
    return frequency_items

# Llamar a la función para ingresar números y obtener la lista
numbers_list = input_numbers()

if numbers_list:
    number_to_remove = int(input("Ingrese el número que desea eliminar: "))  # Solicita el número a eliminar
    remove_number(numbers_list, number_to_remove)  # Llama a la función para eliminar el número
    list_items = f"[{', '.join(map(str, numbers_list))}]"  # Crea una cadena con los elementos de la lista
    sum_items = sum(numbers_list)  # Calcula la suma de los elementos en la lista
    print(f"\nLa sumatoria de los elementos ingresados {list_items} es de: {sum_items}")  # Imprime la suma
else:
    print("La lista de números está vacía.")  # Imprime un mensaje si la lista está vacía

print()  # Salto de Línea

while True:
    try:
        number_limit = int(input("Ingrese un número, para encontrar sus menores: "))  # Solicita un número límite
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")  # Maneja excepciones de tipo ValueError

# Crea una nueva lista con elementos menores que el número límite
numbers_list_limit = [element for element in numbers_list if element < number_limit]

if numbers_list_limit:
    list_items_limit = f"[{', '.join(map(str, numbers_list_limit))}]"  # Crea una cadena con los elementos
    print(f"Los elementos menores a {number_limit} perteneciente a la lista son: {list_items_limit}")  # Imprime la nueva lista
else:
    print(f"La lista no contiene elementos menores a {number_limit}")  # Imprime un mensaje si no hay elementos menores


# Llamar a la función para guardar la tupla con las frecuencias de los elementos 
frequency_items = calculate_frequencies(numbers_list)

print(f"\nLista con sus frecuencias {frequency_items}\n")