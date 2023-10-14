# Solicitar al usuario que ingrese el costo de la cena
costo_cena = float(input("Ingrese el costo de la cena: "))

# Calcular el costo del servicio (6.2% del costo de la cena)
costo_servicio = costo_cena * 0.062

# Calcular el costo de la propina (10% del costo de la cena)
costo_propina = costo_cena * 0.10

# Calcular el costo final sumando la cena, el servicio y la propina
costo_final = costo_cena + costo_servicio + costo_propina

# Mostrar el costo final al usuario
print(f"El costo final de su cena, incluyendo un 6.2% en concepto de servicio y un 10% de propina, es de ${costo_final:.2f}")

