# Solicitar al usuario la cantidad de kilómetros que puede recorrer su moto con 1 litro de combustible
cantidad_kilometros_litro = int(input("Ingrese la cantidad de kilómetros que su moto recorre con 1 litro de combustible: "))

# Solicitar la capacidad del tanque en litros
capacidad_litros = int(input("Ingrese la capacidad (en litros) del tanque de combustible: "))

# Solicitar cuántos kilómetros en total recorrerán
recorrido_kilometros = int(input("Ingrese cuántos kilómetros en total recorrerán: "))

# Validar entradas negativas o cero
if cantidad_kilometros_litro <= 0 or capacidad_litros <= 0 or recorrido_kilometros <= 0:
    print("Por favor, ingrese valores válidos mayores que cero.")
else:
    # Calcular la cantidad de tanques de combustible necesarios
    total_litros_necesarios = recorrido_kilometros / cantidad_kilometros_litro

    # Validar si se necesita un tanque completo adicional
    if total_litros_necesarios % capacidad_litros != 0:
        total_tanques_necesarios = int(total_litros_necesarios // capacidad_litros) + 1
    else:
        total_tanques_necesarios = int(total_litros_necesarios // capacidad_litros)

    print(f"Para recorrer {recorrido_kilometros} kilómetros, necesitará {total_tanques_necesarios} tanques de combustible.")
