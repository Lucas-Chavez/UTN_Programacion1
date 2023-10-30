# Ejercicio 1
numero1 = 20

# Muestro por consola el resultado del ejercicio 1
print(
    f"El valor del primer número es: \"{numero1}\"." 
)

# Salto de línea
print("")

# Ejercicio 2
numero2 = 40

# Muestro por consola el resultado del ejercicio 2
print(
    f"El valor del segundo número es: \"{numero2}\"." 
)

# Salto de línea
print("")

# Ejercicio 3
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Ejercicio 4
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")

# Salto de línea
print("")

# Ejercicio 5
nombre = "Lucas Chavez"

# Ejercicio 6
precio = 50.25

# Ejercicio 7
descuento = 0.25

# Ejercicio 8
precio_final = precio * (1 - descuento)

# Muestro por consola el resultado de los ejercicios 5, 6, 7 y 8
print(
    f"Mi nombre es {nombre}.\n"
    f"Compré un producto con un precio de ${precio:.2f}.\n"
    f"Obtuve un descuento del {descuento * 100}% en mi compra.\n"
    f"Finalmente, pagué ${precio_final:.2f}."
)

# Salto de línea
print("")

# Ejercicio 9
cadena = "Si puedes soñarlo, puedes hacerlo"

# Ejercicio 10
longitud = len(cadena)

# Muestro por consola el resultado de los ejercicios 9, 10
print(
    f"Frase \"{cadena}\".\n"
    f"Longitud frase: {longitud}."
)

# Salto de línea
print("")

# Ejercicio 11
precio = int(56.324)

# Muestro por consola el resultado del ejercicio 11
print(
    f"Precio {precio}$." #Casteo el valor de "precio" a "int"
)

# Salto de línea
print("")

# Ejercicio 12
nombre = "Lucas"
apellido = "Chavez"
nombre_completo = nombre + " " + apellido  # Concateno nombre y apellido con un espacio

# Muestro por consola el resultado del ejercicio 12
print(
    f"Mi nombre completo es: \"{nombre_completo}\"." 
)

# Salto de línea
print("")

# Ejercicio 13
edad = 19
print(f"Mi edad es: {edad}", end=", ")
edad += 5
print(f"mi edad incrementada en 5 es: {edad}", end=", ")
edad -= 10
print(f"mi edad decrementada en 10 es: {edad}")

# Salto de línea
print("")

# Ejercicio 14
altura = 1.70
print(f"Mi altura es: {altura}", end=", ")
altura *= 4
print(f"mi altura multiplicada por 4 es: {altura}", end=", ")
altura /= 3
print(f"mi altura dividida por 3 es: {altura:.2f}")

# Salto de línea
print("")

# Ejercicio 15
mi_nombre = "LUCAS CHAVEZ"
print(f"Mi nombre en minúscula es: {mi_nombre.lower()}")

# Salto de línea
print("")

# Ejercicio 16
print(f"Mi nombre con la primera letra en mayúscula y el resto en minúscula es: {mi_nombre.capitalize()}")

# Salto de línea
print("")