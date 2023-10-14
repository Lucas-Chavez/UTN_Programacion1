# Solicita al usuario la base del rectángulo y la almacena como un número de punto flotante
base_rectangulo = float(input("Digite la base del rectángulo: "))
# Solicita al usuario la altura del rectángulo y la almacena como un número de punto flotante
altura_rectangulo = float(input("Digite la altura del rectángulo: "))
# Calcula el perímetro del rectángulo utilizando la fórmula: 2 * (base + altura)
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
# Imprime el resultado del cálculo del perímetro
print(f"El perímetro del rectángulo es de: {perimetro_rectangulo}")