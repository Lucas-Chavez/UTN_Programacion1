saldo = 0  # Inicializamos el saldo en 0

while True:
    operacion = input("Ingrese la operación (D para depósito, R para retiro, línea vacía para finalizar): ")
    
    # Verificamos si la entrada está vacía para finalizar
    if not operacion:
        break
    
    # Dividimos la operación en tipo (D o R) y cantidad
    tipo, cantidad = operacion.split(" ")
    cantidad = int(cantidad)
    
    # Realizamos la operación correspondiente
    if tipo == 'D':
        saldo += cantidad  # Deposito: sumar a saldo
    elif tipo == 'R' and (saldo - cantidad) >= 0 :
        saldo -= cantidad  # Retiro: restar de saldo
    else:
        print("La operación no se pudo realizar")

# Mostramos el saldo final
print("Saldo final:", saldo)
