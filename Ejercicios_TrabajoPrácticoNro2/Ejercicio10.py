# Solicitar al cliente que ingrese su edad.
entrada_edad = input("Ingrese la edad del cliente: ").strip()

# Comprobar si la entrada es un número válido.
if entrada_edad.isdigit():
    edad_cliente = int(entrada_edad)
    if 4 <= edad_cliente <= 18:
        print("El cliente debe pagar $500 pesos por la entrada.")
    elif edad_cliente > 18:
        print("El cliente debe pagar $1000 pesos por la entrada.")
    else:
        print("El cliente puede entrar de forma gratuita.")
else:
    # Si la entrada no es un número válido, mostrar un mensaje de error.
    print("Por favor, ingrese una edad válida como número entero.")
