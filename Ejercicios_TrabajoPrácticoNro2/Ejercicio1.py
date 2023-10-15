# Solicitar al usuario que ingrese el número de años de su computadora.
anios_computadora = int(input("Ingrese el número de años que tiene su computadora: "))

# Comprobar si la computadora tiene 2 años o menos.
if anios_computadora <= 2:
    print("Su computadora se considera nueva.")
else:
    # Si la computadora tiene más de 2 años, se considera vieja.
    print("Su computadora se considera vieja.")
