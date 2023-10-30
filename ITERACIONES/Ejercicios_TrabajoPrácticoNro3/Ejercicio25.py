import validar  # Importa el módulo de validación

# Solicitamos al usuario que ingrese un número entero positivo
numero = validar.entero_positivo("Ingrese un número positivo: ")

# Inicializamos la variable 'factorial' en 1, ya que el factorial de 0 es 1.
factorial = 1

# Usamos un bucle 'for' para calcular el factorial del número ingresado.
# Comenzamos desde 1 y llegamos hasta el número ingresado.
for i in range(1, numero + 1):
    factorial *= i  # Multiplicamos 'factorial' por 'i' en cada iteración.

# Mostramos el resultado, que es el factorial del número ingresado.
print(f"El factorial de {numero} es {factorial}")

