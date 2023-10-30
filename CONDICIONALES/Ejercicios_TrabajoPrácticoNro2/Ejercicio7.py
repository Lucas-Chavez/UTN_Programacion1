try:
    # Solicitar al usuario que ingrese tres números
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))
    tercer_numero = float(input("Ingrese el tercer número: "))

    # Inicializar la variable para almacenar el número menor
    numero_menor = primer_numero

    # Comprobar si el segundo número es menor que el actual número menor
    if segundo_numero < numero_menor:
        numero_menor = segundo_numero

    # Comprobar si el tercer número es menor que el actual número menor
    if tercer_numero < numero_menor:
        numero_menor = tercer_numero

    print(f"El número menor es: {numero_menor}")

except ValueError:
    print("Por favor, ingrese números válidos.")
