import sys
sys.path.append("C:/Users/Rosamel/Desktop/UTN/GIT-PROGRAMACION/FUNCION")
from Funciones import add_digits  # Importar función para sumar dígitos
from Ejercicio14 import is_prime_number  # Importar función para verificar si es primo
from Ejercicio16 import count_digit_frequency  # Importar función para contar ocurrencias de un dígito
from Ejercicio15 import calculate_factorial  # Importar función para calcular el factorial

number_list = []  # Lista para almacenar números primos

# Solicitar números primos al usuario hasta que ingrese uno que no lo sea
while True:
    try:
        number = int(input("Ingrese un número primo (o un número no primo para salir): "))
        if number < 0:
            print("Por favor, ingrese un número entero positivo válido.")
            continue
        
        if is_prime_number(number):
            number_list.append(number)
        elif not number_list:
            print("Debe ingresar al menos un número primo.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número entero.")

# Solicitar al usuario un dígito para contar
while True:
    try:
        digit = int(input("\nIngrese un dígito para conocer su frecuencia: "))
        if 0 <= digit <= 9:
            break
        else:
            print("Por favor, ingrese un dígito válido (0-9).")
    except ValueError:
        print("Por favor, ingrese un dígito válido.")

# Mostrar encabezados
print(f"\n{'Número':<10} {'Suma digitos':<15} {'Frecuencia ':<15}")

# Mostrar información para cada número primo ingresado
for number in number_list:
    # Calcular la suma de los dígitos y la frecuencia del dígito
    digit_sum = add_digits(number)
    frequency = count_digit_frequency(number, digit)
    # Mostrar la información en una fila
    print(f"{number:<10} {digit_sum:<15} {frequency:<15}")

# Calcular y mostrar el factorial del número primo más grande
bigger_number = max(number_list)
factorial_number = calculate_factorial(bigger_number)
print(f"\nEl factorial del número {bigger_number} es: {factorial_number}")
