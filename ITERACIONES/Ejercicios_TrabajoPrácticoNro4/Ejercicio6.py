# Creamos una lista de números
numeros = [10, 25, 3, 42, 17, 8, 39, 21]

# Número específico que deseamos encontrar
numero_especifico = 17

# Usamos un bucle for para recorrer la lista
for numero in numeros:
    if numero == numero_especifico:
        print(f"Se ha encontramos el número {numero_especifico}")
        break  # Salimos del bucle cuando encontramos el número

# Si no encontramos el número, mostramos un mensaje
else:
    print(f"El número {numero_especifico} no se encontró en la lista.")
