import validar  # Importa el módulo de validación

while True:
    # Solicitamos al usuario que ingrese el monto a pagar
    monto = validar.entrada_flotante("Ingrese el monto a pagar (Digite '0' para finalizar): ")

    if monto < 0:
        # Validamos que el monto sea positivo
        print("Debe ingresar un monto positivo.")
        continue  # Salta al siguiente ciclo si el monto no es positivo.
    else:
        break

if monto > 1000:
    # Aplicar un descuento del 10% si el monto es mayor a $1000
    descuento = 0.10
    monto_final = monto - (monto * descuento)
    print("Se le ha aplicado un descuento del 10%.")
else:
    monto_final = monto

print(f"Su total a pagar es de {monto_final:.2f}")
