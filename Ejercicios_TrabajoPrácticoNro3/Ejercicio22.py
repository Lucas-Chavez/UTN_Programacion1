import validar  # Importa el módulo de validación

# Creamos una lista para almacenar los números
lista_numeros = []

while True:
    # Solicitamos al usuario que ingrese un número entero positivo
    numero = validar.entrada_entero("Ingrese un número positivo (Digite '-1' para salir): ")

    if numero < 0 and numero != -1:
        # Validamos que el número sea positivo y diferente de -1 (opción de salida)
        print("Debe ingresar un número entero positivo.")
        continue  # Salta al siguiente ciclo si el número ingresado no es positivo.

    if numero == -1:
        break  # Si el usuario ingresa -1, salimos del bucle

    lista_numeros.append(numero)  # Agregamos el número a la lista

if lista_numeros:
    contador = 0
    for i in lista_numeros:
        if i % 2 == 0:
            contador += 1
    # Mostramos los número pares ingresados
    print(f"Se han ingresado {contador} números pares")
else:
    print("No se ingresaron números")
