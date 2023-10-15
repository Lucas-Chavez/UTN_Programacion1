# Solicitar al usuario que ingrese dos valores
primer_valor = float(input("Ingrese el primer valor: "))
segundo_valor = float(input("Ingrese el segundo valor: "))

# Solicitar al usuario que elija la operación
print("Elija la operación que desea realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Capturar la elección del usuario
operacion = input("Ingrese el número de la operación que desea realizar: ")

# Verificar la operación seleccionada
if operacion == "1":
    resultado = primer_valor + segundo_valor
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "2":
    resultado = primer_valor - segundo_valor
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "3":
    resultado = primer_valor * segundo_valor
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "4":
    if segundo_valor != 0:  # Evitar división por cero
        resultado = primer_valor / segundo_valor
        print(f"El resultado de la división es: {resultado}")
    else:
        print("No se puede dividir por cero.")
else:
    print("Operación no válida. Ingrese 1, 2, 3 o 4 para realizar una operación válida.")
