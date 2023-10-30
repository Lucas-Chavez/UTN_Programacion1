# Solicitar al usuario que ingrese los nombres y eliminar espacios iniciales o finales y convertir a minúsculas
primer_nombre = input("Ingrese el primer nombre: ").strip().lower()
segundo_nombre = input("Ingrese el segundo nombre: ").strip().lower()

# Verificar si se ingresaron nombres válidos
if primer_nombre and segundo_nombre:
    # Comparar si la primera letra de ambos nombres es la misma
    if primer_nombre[0] == segundo_nombre[0]:
        print("Coincidencia: Ambos nombres comienzan con la misma letra.")
    else:
        print("No hay coincidencia: Los nombres no comienzan con la misma letra.")
else:
    print("Por favor, ingrese nombres válidos.")
