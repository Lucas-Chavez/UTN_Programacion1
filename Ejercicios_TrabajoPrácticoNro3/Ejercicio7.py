# Itera a través de los multiplicandos del 1 al 10
for multiplicando in range(1, 11):
    # Imprime un salto de línea para separar las tablas
    print("\nTabla de multiplicar del", multiplicando)
    # Itera a través de los multiplicadores del 1 al 10
    for multiplicador in range(1, 11):
        # Calcula el producto y convierte los números a cadenas con ceros iniciales para que tengan un formato consistente
        producto = multiplicando * multiplicador
        multiplicando_str = str(multiplicando).zfill(2)
        multiplicador_str = str(multiplicador).zfill(2)
        producto_str = str(producto).zfill(2)
        # Imprime la ecuación y el resultado en un formato ordenado
        print(f"{multiplicando_str} x {multiplicador_str} = {producto_str}")