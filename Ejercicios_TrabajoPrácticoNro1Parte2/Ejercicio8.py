# Solicitar al vendedor que ingrese su sueldo base.
sueldo_base = float(input("Digite su sueldo base: "))
# Solicitar al vendedor el valor de las tres ventas realizadas en el mes.
venta1 = float(input("Digite el valor de la primera venta: "))
venta2 = float(input("Digite el valor de la segunda venta: "))
venta3 = float(input("Digite el valor de la tercera venta: "))
# Calcular la comisión total de ventas como el 10% de la suma de las tres ventas.
comision_ventas = (venta1 + venta2 + venta3) * 0.1
# Calcular el sueldo total sumando el sueldo base y la comisión de ventas.
total_sueldo = sueldo_base + comision_ventas
# Mostrar el sueldo total que el vendedor recibirá en el mes.
print(f"Su sueldo final más las comisiones de las ventas es de: {total_sueldo}")