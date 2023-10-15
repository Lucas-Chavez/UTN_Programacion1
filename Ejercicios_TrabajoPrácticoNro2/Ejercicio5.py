# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ").strip().lower()

# Definir una lista de vocales
vocales = ["a", "e", "i", "o", "u"]

# Verificar si la entrada es válida
if len(letra) == 1:
    if letra in vocales:
        print(f"La letra '{letra}' es una vocal.")
    else:
        print(f"La letra '{letra}' no es una vocal.")
else:
    print("No se puede procesar la entrada. Ingrese solo un carácter.")