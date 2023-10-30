def last_word_length(text_string):
    # Elimina los espacios en blanco al principio y al final de la cadena
    text_string = text_string.strip()
    
    # Divide la cadena en palabras usando los espacios en blanco como separadores
    words = text_string.split()
    
    # Verifica si hay al menos una palabra en la lista de palabras
    if words:
        # Obtiene la última palabra y calcula su longitud
        last_word = words[-1]
        return len(last_word)
    else:
        # Si no hay palabras, retorna 0
        return 0