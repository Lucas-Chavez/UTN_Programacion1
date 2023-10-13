import validar

# Creamos una lista para almacenar los números
lista_numeros = []
while True:
    # Solicitamos al usuario que ingrese un número entero
    numero = validar.entrada_entero("Ingrese un número entero (Digite '0' para salir): ")
    if numero == 0:
        break  # Si el usuario ingresa 0, salimos del bucle
    lista_numeros.append(numero)  # Agregamos el número a la lista
# Sumamos los números en la lista utilizando la función `sum()`
suma = sum(lista_numeros)
# Mostramos la suma de los números ingresados
print(f"La suma de los números ingresados es: {suma}")