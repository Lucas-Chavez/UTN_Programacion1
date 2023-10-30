def add_space_to_string(text_string):
    # Usamos el método join de las cadenas para agregar un espacio tras cada letra
    new_string = " ".join(text_string)

    return new_string

# Solicitamos al usuario una cadena de texto
user_input = input("Ingrese una cadena de texto: ")

# Llamamos a la función y mostramos el resultado
result = add_space_to_string(user_input)
print(result)