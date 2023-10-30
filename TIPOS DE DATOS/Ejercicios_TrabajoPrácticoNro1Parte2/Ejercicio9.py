# Solicitar al usuario el valor de la compra.
valor_compra = float(input("Digite el valor de su compra: "))
# Definir el porcentaje de descuento.
descuento_porcentaje = 15
# Calcular el descuento aplicado.
descuento = valor_compra * (descuento_porcentaje / 100)
# Calcular el precio final con el descuento aplicado.
precio_final = valor_compra - descuento
# Mostrar el precio final al usuario.
print(f"El precio final de su compra con un descuento del {descuento_porcentaje}% es de: {precio_final}")