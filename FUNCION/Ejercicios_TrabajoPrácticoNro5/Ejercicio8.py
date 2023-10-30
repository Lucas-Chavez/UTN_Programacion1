def area_and_perimeter_of_circle(circle_radius):
    import math
    # Calcula el área y el perímetro de la circunferencia utilizando la fórmula matemática.
    PI = math.pi
    area = PI * (circle_radius ** 2)
    perimeter = 2 * PI * circle_radius

    return area, perimeter

# Solicita al usuario ingresar el radio de la circunferencia.
circle_radius = float(input("Ingrese el radio de la circunferencia: "))

if circle_radius > 0:  # Verifica si el radio es un número positivo.
    area_circle, perimeter_circle = area_and_perimeter_of_circle(circle_radius)
    print(f"Área del círculo: {area_circle:.2f}")
    print(f"Perímetro del círculo: {perimeter_circle:.2f}")
else:
    print("El radio debe ser un número positivo.")