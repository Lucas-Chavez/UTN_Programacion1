while True:
    palabra = input("Ingrese una palabra (escriba 'salida' para salir): ")
    # Verifica si el usuario ha ingresado "salida" (sin importar mayúsculas o minúsculas).
    if palabra.lower() == "salida":
        break  # Si se ingresa "salida," sale del bucle while.
    # Itera a través de la longitud de la palabra y muestra rebanadas progresivamente más cortas.
    for i in range(len(palabra), 0, -1):
        print(palabra[:i], end=" ")  # Muestra la rebanada actual, sin saltar de línea.
    print("")  # Imprime una línea en blanco para separar los ecos de las palabras.