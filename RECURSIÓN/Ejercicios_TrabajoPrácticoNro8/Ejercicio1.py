def count_digits(n):
    # Caso base: Si el número es menor que 10, tiene un solo dígito.
    if n < 10:
        return 1
    # Caso recursivo: Divide el número por 10 para eliminar el último dígito y llama recursivamente.
    else:
        return 1 + count_digits(n // 10)

# Ejemplo de uso:
n = 12345
digit_count = count_digits(n)
print(f"El número {n} tiene {digit_count} dígitos.")
