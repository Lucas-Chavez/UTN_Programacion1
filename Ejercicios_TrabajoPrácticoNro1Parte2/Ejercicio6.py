# Solicita al usuario el primer número y lo almacena como un número de punto flotante.
numero1 = float(input("Digite el primer número: "))
# Solicita al usuario el segundo número y lo almacena como un número de punto flotante.
numero2 = float(input("Digite el segundo número: "))
# Solicita al usuario el tercer número y lo almacena como un número de punto flotante.
numero3 = float(input("Digite el tercer número: "))
# Calcula la media de los números ingresados.
media_numeros = (numero1 + numero2 + numero3) / 3
# Imprime el resultado de la media.
print(f"La media de los números es de: {media_numeros:.2f}")