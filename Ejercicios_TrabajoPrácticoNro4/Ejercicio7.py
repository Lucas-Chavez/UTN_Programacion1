while True:
    # Mostrar el menú de opciones
    print("Menú de opciones:")
    print("1. Realizar tarea 1")
    print("2. Realizar tarea 2")
    print("3. Realizar tarea 3")
    print("0. Salir")

    # Solicitar la elección del usuario
    opcion = input("Elija una opción (0 para salir): ")

    if opcion == "0":
        print("Saliendo del programa.")
        break  # Salir del bucle si el usuario elige "0"
    elif opcion == "1":
        print("Realizando la tarea 1...")
    elif opcion == "2":
        print("Realizando la tarea 2...")
    elif opcion == "3":
        print("Realizando la tarea 3...")
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")