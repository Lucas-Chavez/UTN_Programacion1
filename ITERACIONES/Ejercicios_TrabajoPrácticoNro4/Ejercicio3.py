set_numeros = set()  # Creamos un conjunto (set) para almacenar los números ingresados

while True:
    numero = int(input("Ingrese un número mayor que 1 (0 para finalizar): "))
    
    if numero == 0:
        break  # Si se ingresa 0, salimos del bucle
    if numero == 1:
        continue  # Ignoramos el número 1 ya que no es primo

    set_numeros.add(numero)  # Agregamos el número al conjunto

cantidad_primos = 0  # Inicializamos el contador de números primos en 0

for i in set_numeros:
    divisores = 0  # Reiniciamos el contador de divisores en cada iteración
    for e in range(1, i + 1):
        if i % e == 0:
            divisores += 1
    if divisores == 2:  # Un número primo tiene exactamente 2 divisores: 1 y sí mismo
        cantidad_primos += 1

print(f"La cantidad de números primos ingresados es: {cantidad_primos}")
