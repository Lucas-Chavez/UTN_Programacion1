# Solicitar al usuario que ingrese el año, mes y día de su nacimiento
year = input("Digite su año de nacimiento (AAAA): ").strip()
month = input("Digite su mes de nacimiento (MM): ").strip()
day = input("Digite su día de nacimiento (DD): ").strip()

# Comprobar si la fecha es válida (mes <= 12 y día <= 31)
if (
    year.isdigit() and len(year) == 4
    and month.isdigit() and 1 <= int(month) <= 12
    and day.isdigit() and 1 <= int(day) <= 31
):
    # Formatear la fecha en formato DDMMAA con ceros iniciales si es necesario
    fecha = f"{day:0>2}{month:0>2}{year[-2:]}"
    print(f"Fecha de nacimiento en formato DDMMAA: {fecha}")
else:
    print("Fecha no válida. Asegúrese de ingresar valores numéricos válidos para el año, mes y día.")

