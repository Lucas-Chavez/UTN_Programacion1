# Falta definir la variable "nombre" antes de usarla en la función input.
# A = input(nombre, “¿Cuál es tu canción favorita?”)
nombre = input("Ingrese su nombre: ")
A = input(f"Hola, {nombre}. ¿Cuál es tu canción favorita? ")

# Se debe convertir el valor de entrada a un número antes de realizar operaciones aritméticas con él.
# precio = input(“Precio: “)
# total = precio + (precio * 0.1)
precio = float(input("Precio: "))
total = precio + (precio * 0.1)

# Falta un par de comillas en la función print y una coma para concatenar el mensaje con la variable
# edad = int(input(“Edad: “))
# print(tu edad es, edad)
edad = int(input("Edad: "))
print("Tu edad es:", edad)

# Se utiliza sintaxis incorrecta, se deben comparar los valores
# edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad == 18)