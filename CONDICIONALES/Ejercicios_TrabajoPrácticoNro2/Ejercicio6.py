# Solicitar al usuario que ingrese un año
año = input("Ingrese un año: ").strip()

# Verificar si la entrada es un número válido.
if año.isdigit():
    año = int(año)
    es_bisiesto = ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0)
    if es_bisiesto:
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
else:
    print("El año ingresado no es válido. Por favor, ingrese un número válido.")
