x = 0  # Inicializamos x en 0

while x <= 30:  # Comenzamos un bucle while que se ejecuta mientras x sea menor o igual a 30
    x += 1  # Incrementamos el valor de x en 1 en cada iteración

    if x in [4, 6, 10]:
        print(f"Se saltó el valor {x} de x")  # Si x es 4, 6 o 10, se imprime un mensaje y se usa 'continue' para saltar al siguiente ciclo.
        continue

    if x == 15:
        print(f"Se rompió la ejecución del bucle cuando x valía: {x}")  # Si x es 15, se imprime un mensaje y se utiliza 'break' para salir del bucle.
        break

    print(x)  # Si no se cumple ninguna de las condiciones anteriores, simplemente se imprime el valor actual de x.

# El bucle se detiene cuando x es mayor que 30 o cuando se ejecuta una declaración 'break'.


