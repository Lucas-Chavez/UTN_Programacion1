def is_prime_number(number):
    counter = 0
    # Recorremos los números desde 1 hasta el número que queremos verificar
    for i in range(1, number + 1):
        # Si el número es divisible por i, incrementamos el contador
        if number % i == 0:
            counter += 1
    # Un número primo solo tiene 2 divisores: 1 y sí mismo
    # Por lo tanto, si el contador es 2, el número es primo
    return True if counter == 2 else False