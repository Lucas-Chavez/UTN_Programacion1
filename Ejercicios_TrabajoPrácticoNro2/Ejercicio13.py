# Solicitar al usuario que ingrese dos números enteros
primer_numero = input("Ingrese el primer número: ").strip()
segundo_numero = input("Ingrese el segundo número: ").strip()

# Comprobar si los valores ingresados son nulos o no son dígitos
if not primer_numero.isdigit() or not segundo_numero.isdigit():
    print("Uno o ambos valores no son números enteros válidos.")
elif int(primer_numero) <= 0 or int(segundo_numero) <= 0:
    print("No se pueden ingresar valores negativos o nulos.")
else:
    # Convertir los valores ingresados a enteros
    primer_numero = int(primer_numero)
    segundo_numero = int(segundo_numero)

    # Determinar cuál número es mayor y cuál es menor
    mayor = max(primer_numero, segundo_numero)
    menor = min(primer_numero, segundo_numero)

    # Verificar si el número mayor es múltiplo del número menor
    if mayor % menor == 0:
        print(f"El número {mayor} es múltiplo del número {menor}.")
    else:
        print(f"El número {mayor} no es múltiplo del número {menor}.")
