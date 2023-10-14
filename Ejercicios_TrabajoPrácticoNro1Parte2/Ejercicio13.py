# Solicitar al usuario que ingrese un número de dos cifras
numero = int(input("Ingrese un número de dos cifras: "))

# Verificar si el número tiene dos cifras
if 10 <= numero <= 99:
    # Convertir el número en una cadena, invertirla y luego convertirla nuevamente a entero
    numero_invertido = str(numero)
    numero_invertido = int(numero_invertido[::-1])

    # Mostrar el número invertido
    print(f"El número invertido de {numero} es {numero_invertido}")
else:
    print("El número ingresado no es de dos cifras.")
