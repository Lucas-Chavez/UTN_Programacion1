def pascal(n, k):
    if k == 0 or k == n:
        # Los valores en los bordes del Triángulo de Pascal son siempre 1.
        return 1
    else:
        # Los demás valores se calculan sumando los dos valores contiguos de la fila de arriba.
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Ejemplo de uso:
n = 5
k = 2
result = pascal(n, k)
print(f"El valor en la fila {n} y columna {k} del Triángulo de Pascal es: {result}")