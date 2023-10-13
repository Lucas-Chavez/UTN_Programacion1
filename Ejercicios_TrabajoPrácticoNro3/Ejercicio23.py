import validar  # Importa el módulo de validación

# Creamos una lista para almacenar los montos de compra
lista_compras = []

while True:
    # Solicitamos al usuario que ingrese el monto de la compra
    compra = validar.entrada_flotante("Ingrese el monto de la compra (Digite '0' para finalizar): ")

    if compra < 0:
        # Validamos que el monto de compra sea positivo
        print("Debe ingresar un monto de compra positivo.")
        continue  # Salta al siguiente ciclo si el monto no es positivo.

    if compra == 0:
        break  # Si el usuario ingresa 0, salimos del bucle

    lista_compras.append(compra)  # Agregamos el monto a la lista de compras

monto_final = sum(lista_compras)
# Mostramos el monto final de las compras y lo limitamos a dos decimales 
print(f"El monto final de su compra es de: ${monto_final:.2f}")