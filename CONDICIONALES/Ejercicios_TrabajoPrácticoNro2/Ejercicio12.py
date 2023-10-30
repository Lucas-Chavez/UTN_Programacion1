# Solicitar al usuario que ingrese el año actual y un año aleatorio
anio_actual = input("Ingrese el año actual (Formato AAAA): ").strip()
anio_aleatorio = input("Ingrese un año (Formato AAAA): ").strip()

# Comprobar si los valores ingresados son válidos
if (len(anio_actual) and len(anio_aleatorio) == 4) and (anio_actual.isdigit() and anio_aleatorio.isdigit()):
    
    # Convertir los valores ingresados a enteros
    anio_actual = int(anio_actual)
    anio_aleatorio = int(anio_aleatorio)

    # Calcular la diferencia de años
    anios_faltantes = abs(anio_actual - anio_aleatorio)  

    # Comprobar si el año actual es mayor o menor que el año aleatorio
    # Determinar si se están buscando años futuros o pasados
    if anio_actual > anio_aleatorio:
        print(f"Faltan {anios_faltantes} años para llegar a {anio_aleatorio}.")
    elif anio_actual < anio_aleatorio:
        print(f"Ha pasado desde el año {anio_aleatorio} un total de {anios_faltantes} años.")
    else:
        print("Los años son iguales, no hay diferencia.")
else:
    print("El formato ingresado no es válido. Por favor, ingrese años en formato AAAA.")