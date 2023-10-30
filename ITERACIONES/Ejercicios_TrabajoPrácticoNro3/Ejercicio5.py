import validar

# Solicitar la cantidad a invertir
inversion = validar.flotante_positivo("Ingrese la cantidad a invertir: ")

# Solicitar la tasa de interés anual
tasa_interes_anual = validar.entrada_flotante("Ingrese la tasa de interés anual (en porcentaje): ")

# Solicitar el número de años de inversión utilizando la función de entero positivo
anios = validar.entero_positivo("Ingrese el número de años de la inversión: ")

# Convertir la tasa de interés anual a la tasa de interés decimal
tasa_interes_decimal = tasa_interes_anual / 100

# Calcular el capital obtenido en la inversión para cada año y mostrarlo
for anio in range(1, anios + 1):
    capital_obtenido = inversion * (1 + tasa_interes_decimal)
    print(f"Año {anio}: Capital obtenido = {capital_obtenido:.2f}")
    inversion = capital_obtenido  # Actualizar la inversión para el próximo año