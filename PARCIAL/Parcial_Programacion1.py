# Solicita el nombre del usuario
username = input("Ingrese su nombre: ").strip()

# Muestra un mensaje de bienvenida
print(f"Bienvenido, {username}. Seleccione una opción:")
print("1. Juego de números")
print("2. Juego de palabras")

# Bucle para asegurarse de que el usuario elija una opción válida (1 o 2)
while True:
    option = input("Ingrese el número de su elección: ")

    # Verifica si la entrada es un dígito
    if option.isdigit():
        option = int(option)
        # Comprueba que la opción esté dentro del rango válido (1 o 2)
        if 1 <= option <= 2:
            break
    print("Opción no válida. Ingrese 1 o 2.")

print("")

if option == 1:
    # Opción 1: Juego de números
    numbers = []

    while True:
        user_input = input("Ingrese un número (0 para salir): ").strip()

        # Verifica si la entrada es un dígito
        if user_input.isdigit():
            user_input = int(user_input)

            # Si el usuario ingresa 0, sale del bucle
            if user_input == 0:
                break

            # Agrega el número a la lista de números
            numbers.append(user_input)
        else:
            print("Entrada no válida. Por favor, ingrese un número entero válido.")

    # Filtra números pares e impares
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    if even_numbers:
        # Calcula y muestra el número par más grande
        max_even = max(even_numbers)
        print(f"El mayor número par es: {max_even}")
    else:
        print("No se han ingresado números pares")

    if odd_numbers:
        # Calcula y muestra el promedio de los números impares
        average_odd = sum(odd_numbers) / len(odd_numbers)
        print(f"El promedio de los números impares es: {average_odd}")
    else:
        print("No se han ingresado números impares")

else:
    # Opción 2: Juego de palabras
    phrase = input("Ingrese una frase: ").strip().lower()

    if phrase:
        # Inicializa un diccionario para contar las vocales
        vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        # Itera sobre cada carácter en la frase
        for char in phrase:
            if char in vowel_counts:
                # Incrementa el contador de la vocal correspondiente
                vowel_counts[char] += 1

        # Muestra la cantidad de cada vocal en la frase
        print(f"La frase '{phrase}' contiene:")

        # Itera a través del diccionario vowel_counts, donde cada clave (vowel) representa una vocal y el valor (count) la cantidad de veces que aparece en la frase.
        for vowel, count in vowel_counts.items():
        # Comprueba si count (la cantidad de la vocal) es mayor que cero, lo que significa que la vocal está presente en la frase.
            if count > 0:
                # Si count es mayor que cero, muestra un mensaje indicando cuántas veces aparece la vocal y la vocal en sí.
                print(f"{count} vocal(es) '{vowel}'")
        else:
            # Si count es igual a cero, significa que la vocal no está en la frase, por lo que muestra un mensaje indicando que no se encontraron vocales en la frase.
            print("La frase no contiene ninguna vocal")

    else:
        print("No se ha ingresado ninguna frase.")