# Solicita al usuario el primer número y lo almacena como un número de punto flotante.
numero1 = float(input("Digite el primer número: "))
# Solicita al usuario el segundo número y lo almacena como un número de punto flotante.
numero2 = float(input("Digite el segundo número: "))
# Realiza la suma de los dos números ingresados.
suma = numero1 + numero2
# Realiza la resta de los dos números ingresados.
resta = numero1 - numero2
# Realiza la multiplicación de los dos números ingresados.
multiplicacion = numero1 * numero2
# Realiza la división del primer número entre el segundo número.
division = numero1 / numero2
# Imprime los resultados de las operaciones en pantalla.
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")