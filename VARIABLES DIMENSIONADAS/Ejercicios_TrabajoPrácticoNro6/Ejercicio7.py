# Crear un diccionario para almacenar las ocurrencias de cada carácter
character_counts = {}

# Contador para el número de strings procesados
processed_strings = 0

while processed_strings < 50:
    # Solicitar al usuario que ingrese un string
    user_input = input("Ingrese un string (o 'x' para finalizar): ").lower()

    # Verificar si el usuario quiere finalizar
    if user_input == 'x':
        break

    # Procesar el string ingresado
    for char in user_input:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    # Incrementar el contador de strings procesados
    processed_strings += 1

# Mostrar la cantidad total de ocurrencias de cada carácter
print("\nCantidad total de ocurrencias de cada carácter:")
for char, count in character_counts.items():
    print(f"'{char}': {count}")