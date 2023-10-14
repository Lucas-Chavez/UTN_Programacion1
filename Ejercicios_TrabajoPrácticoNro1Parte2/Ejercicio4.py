# Solicita al usuario ingresar los grados Fahrenheit.
grados_fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
# Realiza la conversión de grados Fahrenheit a grados Celsius.
grados_celsius = (grados_fahrenheit - 32) * 5 / 9
# Muestra en pantalla la conversión de Fahrenheit a Celsius.
print(f"{grados_fahrenheit} grados Fahrenheit son equivalentes a {grados_celsius:.2f} grados Celsius.")