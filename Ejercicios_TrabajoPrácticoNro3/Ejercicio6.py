import validar

# Solicita al usuario que ingrese la altura del triángulo rectángulo
mensaje = "Ingrese la altura del triángulo rectángulo: "
# Solicitar la altura del triángulo rectángulo utilizando la función de validar entero positivo
altura = validar.entero_positivo(mensaje)
# Itera desde 1 hasta la altura ingresada (incluyendo la altura)
for i in range(1, altura + 1):
    # Imprime una línea con '*' repetidos 'i' veces, donde 'i' es el número de la iteración actual
    print(f"{'*' * i}")