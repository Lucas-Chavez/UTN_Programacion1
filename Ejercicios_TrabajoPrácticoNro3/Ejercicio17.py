while True:
    # Solicitar al usuario que ingrese una frase y convertirla a minúsculas
    frase = input("Ingrese una frase: ").strip().lower()
    # Validar que se haya ingresado una frase
    if not frase:
        print("Debes ingresar una frase.")
    else:
        break
# Definir las vocales
vocales = ["a", "e", "i", "o", "u"]
# Crear un conjunto de las vocales que aparecen en la frase
vocales_frase = {letra for letra in frase if letra in vocales}
# Mostrar las vocales encontradas
if vocales_frase:
    print(f'Vocales que aparecen en la frase "{frase.capitalize()}": {", ".join(vocales_frase)}')
else:
    print(f'No se encontraron vocales en la frase "{frase.capitalize()}".')