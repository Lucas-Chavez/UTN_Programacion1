# Inicializa una lista para almacenar las líneas de entrada
lineas = []

# Lee las líneas de entrada hasta que se ingrese una línea en blanco
while True:
    linea = input("Ingrese una línea (deje en blanco para finalizar): ")
    if not linea:
        break  # Sale del bucle si se ingresa una línea en blanco
    lineas.append(linea)  # Agrega la línea a la lista

# Imprime las líneas en mayúsculas
for linea in lineas:
    print(linea.upper())