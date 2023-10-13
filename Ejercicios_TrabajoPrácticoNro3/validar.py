def entero_positivo(mensaje):
    while True:
        try:
            # Solicita al usuario un valor entero y muestra el mensaje proporcionado
            entrada = input(mensaje)
            # Verifica si la entrada es una cadena de dígitos y si es un número positivo
            if not entrada.isdigit() or int(entrada) < 0:
                raise ValueError("Debe ingresar un número entero positivo.")
            # Convierte la entrada válida a un entero y la retorna
            return int(entrada) #Salimos del bucle si la entrada es válida
        except ValueError as e:
            print(f"Error: {e}")

def entrada_entero(mensaje):
    while True:
        try:
            entrada = int(input(mensaje))
            return entrada
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def flotante_positivo(mensaje):
    while True:
        try:
            entrada = float(input(mensaje))  # Solicitamos una entrada al usuario y la convertimos a un número de punto flotante
            if entrada < 0:
                raise ValueError("Debe ingresar un número positivo.")
            return entrada
        except ValueError as e:
            if str(e) == "could not convert string to float: ":
                print("Error: Debe ingresar un número válido.")
            else:
                print(f"Error: {e}")

def entrada_flotante(mensaje):
    while True:
        try:
            entrada = float(input(mensaje))
            return entrada
        except ValueError:
            print("Error: Debe ingresar un número válido.")

