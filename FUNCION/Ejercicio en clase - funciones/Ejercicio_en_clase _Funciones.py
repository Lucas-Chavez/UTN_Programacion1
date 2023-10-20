import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('C:/Users/chave/OneDrive/Escritorio/GIT-PROGRAMACION/FUNCION')

# Importamos el módulo "Funciones" que contiene las funciones "add_digits" y "addition_number".
import Funciones

# Creamos una lista vacía llamada "list_numbers" para almacenar los resultados de "add_digits".
list_numbers = []

while True:
    # Solicitamos al usuario que ingrese una opción (S/N) y la convertimos a minúsculas y eliminamos espacios.
    option = input("¿Desea ingresar un número? (S/N): ").strip().lower()

    if option == "n":
        break

    elif option == "s":
        while True:
            try:
                number = input("Ingrese un número entero: ")

                if not number.isdigit():
                    # Para garantizar que el valor ingresado por el usuario sea un número entero positivo.
                    # Se lanza una excepción ValueError para manejar este error.
                    raise ValueError("El argumento debe ser un número entero positivo")

                # Convertimos la entrada del usuario a un número entero.
                number = int(number)
                # Llamamos a la función "add_digits" del módulo "Funciones" y agregamos el resultado a la lista "list_numbers".
                list_numbers.append(Funciones.add_digits(number))
                break

            # Si se produce una excepción capturamos la excepción y mostramos un mensaje de error.
            except ValueError as e:
                print("Error: " + str(e))

    else:
        print("La opción ingresada no es válida")

# Llamamos a la función "addition_number" del módulo "Funciones" y pasamos la lista "list_numbers" como argumento.
total_sum = Funciones.addition_number(list_numbers)

# Imprimimos el resultado.
print("La suma de los dígitos ingresados es:", total_sum)
