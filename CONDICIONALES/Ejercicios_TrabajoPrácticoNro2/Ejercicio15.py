print("¿De qué figura desea calcular el área?")
print("1. Triángulo (Ingrese 'T' o 't')")
print("2. Círculo (Ingrese 'C' o 'c')")

# Pedir al usuario que seleccione una opción
seleccion_usuario = input("Ingrese una opción: ").lower()

# Verificar la selección del usuario
if seleccion_usuario == "t":
    # Calcular el área de un triángulo
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    
    area_triangulo = (base_triangulo * altura_triangulo) / 2
    print(f"El área del triángulo es: {area_triangulo}")
elif seleccion_usuario == "c":
    # Calcular el área de un círculo
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    PI = 3.14159  # Usamos una aproximación más precisa de PI

    area_circulo = PI * (radio_circulo ** 2)
    print(f"El área del círculo es: {area_circulo}")
else:
    print("La opción seleccionada no es válida. Ingrese 'T' o 'C' para calcular el área.")
