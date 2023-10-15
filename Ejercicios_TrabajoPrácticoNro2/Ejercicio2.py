# Solicitar al usuario que ingrese el número de años de su computadora y eliminar espacios en blanco alrededor.
anios_computadora = input("Ingrese el número de años que tiene su computadora: ").strip()

# Comprobar si la entrada es un número válido.
if anios_computadora.isdigit():
    anios_computadora = int(anios_computadora)  # Convertir la entrada a un entero.
    # Comprobar si la computadora tiene 2 años o menos.
    if anios_computadora <= 2:
        print("Su computadora se considera nueva.")
    else:
        # Si la computadora tiene más de 2 años, se considera vieja.
        print("Su computadora se considera vieja.")
else:
    # Si la entrada no es un número válido, mostrar un mensaje de error.
    print("Por favor, ingrese un número de años válido para su computadora.")

