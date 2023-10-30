# Solicitar al usuario que ingrese la cantidad de lápices que desea comprar.
cantidad_lapices = int(input("Ingrese la cantidad de lápices: "))

# Definir como constante el costo por lápiz y el porcentaje de descuento si se compran 1000 o más lápices.
COSTO_LAPICES = 60
DESCUENTO = 0.07
LAPICES_PARA_DESCUENTO = 1000

# Calcular el costo total antes de aplicar cualquier descuento.
total_pagar = cantidad_lapices * COSTO_LAPICES

# Verificar si la cantidad de lápices supera o es igual a la cantidad requerida para aplicar el descuento.
if cantidad_lapices >= LAPICES_PARA_DESCUENTO:
    # Calcular el monto del descuento.
    descuento = total_pagar * DESCUENTO
    # Restar el descuento al costo total.
    total_pagar -= descuento

# Mostrar el monto total a pagar al usuario.
print(f"Debe pagar por {cantidad_lapices} lápices un total de: ${total_pagar}")
