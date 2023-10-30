import random

def add_digits(number):
    try:
        if not isinstance(number, int):
            raise ValueError("El argumento debe ser un número entero")

        add = 0
        for digit in str(number):
            add += int(digit)
        return add
        
    except ValueError as e:
        return "Error: " + str(e)
    
def addition_number(list_numbers):
    addition = sum(list_numbers)
    return addition

# Función para crear una lista con elementos aleatorios
def create_random_list(length, min_value, max_value):
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list

# Función para mostrar una lista
def display_list(input_list):
    show_list = f"[{', '.join(str(number) for number in input_list)}]"
    print(show_list)