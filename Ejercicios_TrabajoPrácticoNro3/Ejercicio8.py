import validar

# Solicitar la altura del triángulo rectángulo utilizando la función de validar entero positivo
altura = validar.entero_positivo("Ingrese la altura del triángulo rectángulo: ")

# Recorremos desde 1 hasta (altura*2) + 1 con incrementos de 2 para construir el triángulo.
for i in range(1, (altura * 2) + 1, 2):
    mensaje = ""
    # Para cada fila del triángulo, retrocedemos de 2 en 2 desde i hasta 0.
    for e in range(i, 0, -2):
        mensaje += str(e) + " "
    print(mensaje)

