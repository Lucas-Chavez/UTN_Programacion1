# Función para calcular el factorial de un número
def calculate_factorial(number):
    if number < 0:
        return None  # El factorial no está definido para números negativos
    elif number == 0:
        return 1  # El factorial de 0 es 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial

def counter_numbers():
    # Inicializar un contador para el número de números leídos
    counter = 0
    while True:
        try:
            input_number = int(input("Ingrese un número (o un valor negativo para salir): "))
            
            # Salir del bucle si se ingresa un número negativo
            if input_number < 0:
                break
            
            # Incrementar el contador de números leídos
            counter += 1
            
            # Calcular y mostrar el factorial
            factorial = calculate_factorial(input_number)
            print(f"El factorial de {input_number} es {factorial}")
            
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print(f"Se leyeron un total de {counter} números.")
