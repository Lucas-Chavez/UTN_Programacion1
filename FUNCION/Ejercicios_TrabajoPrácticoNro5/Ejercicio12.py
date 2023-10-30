# Definición de la función dictionary_word_length que recibe una frase como entrada.
def dictionary_word_length(phrase):
    # Dividir la frase en palabras utilizando un espacio en blanco como separador y almacenarlas en la lista 'words'.
    words = phrase.split()
    
    # Usar una comprensión de diccionario para crear un diccionario que asocie cada palabra con su longitud.
    # El resultado es un diccionario que contiene las palabras de la frase como claves y sus longitudes como valores.
    return {word: len(word) for word in words}

# Definir una frase de ejemplo.
phrase = "Todo lo que se puede imaginar es real"

# Llamar a la función dictionary_word_length con la frase de ejemplo y almacenar el resultado en la variable 'result'.
result = dictionary_word_length(phrase)

# Imprimir el diccionario resultante que contiene las palabras y sus longitudes.
print(result)



