# Definición de la función para contar la frecuencia de un dígito en un número
def count_digit_frequency(number, digit):
    # Verificar que tanto 'number' como 'digit' sean números enteros
    if str(number).isdigit() and str(digit).isdigit():
        # Usar 'str(number)' para convertir 'number' a una cadena y luego contar las ocurrencias de 'str(digit)' en esa cadena
        count = str(number).count(str(digit))
        return count
    return  # Devolver none si 'number' o 'digit' no son números enteros válidos