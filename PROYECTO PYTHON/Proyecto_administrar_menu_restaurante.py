def validate_positive_integer(message):
    while True:
        try:
            number = int(input(message))  # Solicita al usuario ingresar un número entero.
            if number > 0:
                return number  # Devuelve el número si es mayor que cero.
            else:
                print("Debe ingresar un número mayor que cero.")  # Muestra un mensaje de error si el número no es válido.
        except ValueError:
            print("Debe ingresar un número entero válido.")  # Muestra un mensaje de error si la entrada no es un número.

def show_plates(food_menu, menu_prices):
    print("")  # Imprime un salto de línea para una mejor presentación.
    menu = {}
    for i in range(len(food_menu)):
        menu[i + 1] = (food_menu[i], menu_prices[i])  # Crea un diccionario para almacenar los platos y precios.

    max_len = max(len(dish[0]) for dish in menu.values())  # Encuentra la longitud máxima de un nombre de plato.

    print("Menú:")  # Imprime el título del menú.
    for i, (dish, price) in menu.items():
        print(f"{i}_ {dish.ljust(max_len)}: ${price}")  # Muestra el número de plato, el nombre alineado a la izquierda y el precio.

def add_dish_to_ticket(plate_price, selected_dishes, food_menu, menu_prices):
    while True:
        print("")  # Imprime un salto de línea para una mejor presentación.
        add_dish = validate_positive_integer("Ingrese el número del plato correspondiente: ")  # Solicita al usuario el número del plato a agregar.
        if 1 <= add_dish <= len(food_menu):
            # Si el número de plato es válido, agrega el plato y su precio al ticket.
            selected_dishes.append(food_menu[add_dish - 1])
            plate_price.append(menu_prices[add_dish - 1])
            print(f"El plato '{food_menu[add_dish - 1]}' se ha agregado correctamente")  # Informa al usuario que el plato se ha agregado con éxito.
            break  # Sale del bucle para evitar que el usuario agregue más de un plato a la vez.
        print("El número del plato ingresado no es válido")  # Informa al usuario si el número del plato no es válido.

def remove_plate_from_ticket(plate_price, selected_dishes):
    while True:
        print("")  # Imprime un salto de línea para una mejor presentación.
        show_plates(selected_dishes, plate_price)  # Muestra los platos disponibles en el ticket con sus precios.
        remove_dish = validate_positive_integer("Ingrese el número del plato correspondiente: ")  # Solicita al usuario el número del plato a eliminar.
        if 1 <= remove_dish <= len(selected_dishes):
            # Si el número de plato a eliminar es válido, elimina el plato del ticket y muestra un mensaje de confirmación.
            removed_dish = selected_dishes.pop(remove_dish - 1)
            removed_price = plate_price.pop(remove_dish - 1)
            print(f"El plato '{removed_dish}' se ha eliminado correctamente")
            break  # Sale del bucle para evitar que el usuario elimine más de un plato a la vez.
        print("El número del plato ingresado no es válido")  # Informa al usuario si el número del plato no es válido.

def choose_payment_method():
    print("")  # Imprime un salto de línea para una mejor presentación.
    # Define los métodos de pago disponibles y los descuentos asociados.
    payment_method = {
        'C': ("Pago en efectivo (Ingrese 'C')", 0),
        'TD': ("Tarjeta de débito (Ingrese 'TD')", 0.5),
        'TC': ("Tarjeta de crédito (Ingrese 'TC')", 0.10)
    }

    while True:
        print("Opciones de pago: ")
        for method, option in payment_method.items():
            print(f"{method} = {option[0]}")  # Muestra las opciones de pago y sus descripciones.

        choice = input("Ingrese la opción de pago correspondiente: ").upper()  # Solicita al usuario que elija una opción.

        if choice in payment_method:
            selected_option = payment_method[choice]  # Obtiene la opción de pago seleccionada.
            method_name = selected_option[0].split(" (")[0]  # Obtiene el nombre del método de pago sin la descripción.
            discount_method = selected_option[1]  # Obtiene el descuento asociado al método.
            print(f"Usted ha seleccionado: {method_name}")  # Muestra el método de pago seleccionado.
            print(f"Su descuento es de: {discount_method*100}%")  # Muestra el descuento correspondiente.
            return discount_method  # Retorna el descuento para su uso en el ticket o proceso de pago.

def show_ticket(selected_dishes, plate_price, discount_method):

    if discount_method is None:
        print("No se ha seleccionado ningún método de pago") # Informa al usuario que no se ha seleccionado ningún método de pago.
        return None  # Retorna el valor None para salir de la función.

    print("")  # Imprime un salto de línea para una mejor presentación.
    show_plates(selected_dishes, plate_price)  # Llama a la función para mostrar los platos seleccionados y sus precios.

    # Calcula los precios descontados aplicando el descuento correspondiente.
    discounted_prices = [price - price * discount_method for price in plate_price]

    # Calcula el precio total sumando los precios descontados de los platos.
    total_price = sum(discounted_prices)

    # Muestra el precio total y el descuento aplicado.
    print(f"Su total a pagar con un descuento del {discount_method*100}% es de ${total_price}")

food_menu = [
    "Milanesa a la napolitana",
    "Bife de chorizo a la parrilla con ensalada",
    "Ravioles de ricota y espinaca con salsa de tomate",
    "Pechuga de pollo rellena con jamón y queso con puré de papas",
    "Lomo de cerdo glaseado con miel y vegetales asados"
]
menu_prices = [
    350,
    450,
    320,
    380,
    420
]

selected_dishes = []  # Almacena los platos seleccionados por el usuario.
plate_price = []  # Almacena los precios correspondientes a los platos seleccionados.
discount_method = None  # Inicializa el método de descuento en None (sin valor).

while True:
    print("")
    print("1-Mostrar Menú")
    print("2-Agregar plato al ticket")
    print("3-Quitar plato del ticket")
    print("4-Elegir método de pago")
    print("5-Mostrar ticket")
    print("0-Salir")

    choice = input("Elija una opción (Ingrese '0' para salir): ")

    if choice == '0':
        break # Sale del bucle y finaliza el programa 
    elif choice == '1':
        show_plates(food_menu, menu_prices)  # Muestra el menú al usuario.
    elif choice == '2':
        add_dish_to_ticket(plate_price, selected_dishes, food_menu, menu_prices)  # Permite agregar platos al ticket.
    elif choice == '3' and len(selected_dishes) > 0:
        remove_plate_from_ticket(plate_price, selected_dishes)  # Permite quitar platos del ticket.
    elif choice == '4' and len(selected_dishes) > 0:
        discount_method = choose_payment_method()  # Permite elegir un método de pago y aplica un descuento.
    elif choice == '5' and len(selected_dishes) > 0:
        show_ticket(selected_dishes, plate_price, discount_method)  # Muestra el ticket con los detalles de la orden.

    else:
        print("Opción no válida. Por favor, elija una opción del menú.")