# Definición de la función que aplica descuentos al carrito
def apply_discount(cart, discounts):
    total_price = 0  # Inicializamos el precio total en 0

    # Recorremos el carrito de compra (un diccionario) con productos y precios
    for product, price in cart.items():
        if product in discounts:  # Verificamos si el producto tiene un descuento definido
            discount_percentage = discounts[product]  # Obtenemos el porcentaje de descuento
            discounted_price = price - (price * discount_percentage / 100)  # Calculamos el precio con descuento
            total_price += discounted_price  # Agregamos el precio con descuento al total
        else:
            total_price += price  # Si no hay descuento, agregamos el precio original al total

    return round(total_price, 2)  # Redondea el resultado a 2 decimales