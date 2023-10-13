import validar  # Importa el módulo de validación

# Creamos una lista para almacenar los números
lista_numeros = []

while True:
    # Solicitamos al usuario que ingrese un número entero positivo
    numero = validar.entrada_entero("Ingrese un número positivo (Digite '0' para salir): ")

    if numero < 0:
        print("Debe ingresar un número entero positivo.")
        continue  # Salta al siguiente ciclo si el número ingresado no es positivo.

    if numero == 0:
        break  # Si el usuario ingresa 0, salimos del bucle

    lista_numeros.append(numero)  # Agregamos el número a la lista

# Comprobamos si la lista no está vacía antes de encontrar el número mayor
if lista_numeros:
    # Mostramos el número mayor de los números ingresados
    print(f"El número mayor de los números ingresados es: {max(lista_numeros)}")
else:
    print("No se ingresaron números, no hay un número mayor.")
