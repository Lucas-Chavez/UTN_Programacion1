# Solicitar al usuario dos años
año_inicio = int(input("Ingrese el año de inicio: "))
año_fin = int(input("Ingrese el año de fin: "))

# Inicializar una lista para almacenar los años que cumplen las condiciones
años_cumplen_condiciones = []

# Iterar a través de los años en el rango y verificar si son bisiestos y múltiplos de 10
for año in range(min(año_inicio, año_fin), max(año_inicio, año_fin) + 1):
    # Verificar si el año es bisiesto y múltiplo de 10
    if ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and (año % 10 == 0):
        # Si cumple ambas condiciones, agregarlo a la lista
        años_cumplen_condiciones.append(año)

# Verificar si se encontraron años que cumplan las condiciones
if años_cumplen_condiciones:
    # Usamos una comprensión de lista para convertir los años a cadenas y luego unimos con una coma y espacio
    cadena = ", ".join([str(i) for i in años_cumplen_condiciones])
    print(f"Años bisiestos y múltiplos de 10 encontrados: {cadena}")
else:
    print("No se encontraron años que cumplan ambas condiciones.")
