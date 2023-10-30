def determine_maximum_and_minimum(list_numbers):
    # Utiliza las funciones `max` y `min` para encontrar el máximo y el mínimo de la lista.
    maximum_number = max(list_numbers)
    minimum_number = min(list_numbers)
    return maximum_number, minimum_number

# Solicita al usuario ingresar números separados por espacios y crea una lista.
user_input = input("Ingrese números separados por espacios: ")
input_numbers = user_input.split()

# Convierte los números ingresados a enteros.
numbers = [int(num) for num in input_numbers]

if numbers:  # Verifica si la lista no está vacía.
    max_number, min_number = determine_maximum_and_minimum(numbers)
    print(f"El número máximo es {max_number} y el número mínimo es {min_number}")
else:
    print("No se ingresaron números válidos.")