import validar

# Solicitar al usuario los dos números enteros.
numero1 = validar.entrada_entero("Ingrese el primer número entero: ")
numero2 = validar.entrada_entero("Ingrese el segundo número entero: ")
print(f"Los números impares y pares desde {min(numero1, numero2)} a {max(numero1, numero2)} son:")

# Usar min() y max() para determinar los límites correctamente.
pares = [str(i) for i in range(min(numero1, numero2), max(numero1, numero2) + 1) if i % 2 == 0]
impares = [str(i) for i in range(min(numero1, numero2), max(numero1, numero2) + 1) if i % 2 != 0]

# Utilizar el método str.join() para combinar los elementos de la lista en una cadena.
print(f'Los números pares son: {", ".join(pares)}')
print(f'Los números impares son: {", ".join(impares)}')