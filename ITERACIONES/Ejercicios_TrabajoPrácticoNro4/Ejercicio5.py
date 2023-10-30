# Inicializamos una lista para almacenar los números pares
numeros_par = list()

# Iteramos a través de los números del 1 al 20
for i in range(1, 21):
    # Verificamos si el número es impar, y si es así, omitimos los números impares
    if i % 2 != 0:
        continue
    
    # Si llegamos aquí, el número es par, lo convertimos a cadena y lo agregamos a la lista
    numeros_par.append(str(i))

# Usamos join para formatear la lista de números pares como una cadena
resultado = ", ".join(numeros_par)

# Imprimimos la cadena resultante
print(resultado)

