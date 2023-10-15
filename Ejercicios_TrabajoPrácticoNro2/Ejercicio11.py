# Saludo inicial
print("Bienvenido a la Pizzería Bella Napoli")
print("Por favor, seleccione el tipo de pizza que desea:")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")

# Solicitar al usuario que ingrese la opción de pizza
opcion_pizza = input("Ingrese el número de su elección: ")

# Comprobar si el usuario seleccionó una pizza vegetariana
if opcion_pizza == "1":
    print("Ingredientes disponibles para la Pizza Vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
    opcion_ingrediente = input("Elija un ingrediente (ingrese el número correspondiente): ")

    # Asignar la pizza vegetariana elegida en función del ingrediente seleccionado
    if opcion_ingrediente == "1":
        pizza = "Pizza Vegetariana con Pimiento, Mozzarella y Tomate"
    elif opcion_ingrediente == "2":
        pizza = "Pizza Vegetariana con Tofu, Mozzarella y Tomate"
    else:
        # Mensaje de error si se ingresa una opción no válida
        print("Opción no válida")
        pizza = "Desconocida"

# Comprobar si el usuario seleccionó una pizza no vegetariana
elif opcion_pizza == "2":
    print("Ingredientes disponibles para la Pizza no Vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    opcion_ingrediente = input("Elija un ingrediente (ingrese el número correspondiente): ")

    # Asignar la pizza no vegetariana elegida en función del ingrediente seleccionado
    if opcion_ingrediente == "1":
        pizza = "Pizza no Vegetariana con Peperoni, Mozzarella y Tomate"
    elif opcion_ingrediente == "2":
        pizza = "Pizza no Vegetariana con Jamón, Mozzarella y Tomate"
    elif opcion_ingrediente == "3":
        pizza = "Pizza no Vegetariana con Salmón, Mozzarella y Tomate"
    else:
        # Mensaje de error si se ingresa una opción no válida
        print("Opción no válida")
        pizza = "Desconocida"

# Mensaje de error si se ingresa una opción no válida
else:
    print("Opción no válida")
    pizza = "Desconocida"

# Mostrar la pizza seleccionada o un mensaje de error
print(f"Su pizza contiene los siguientes ingredientes: {pizza}")