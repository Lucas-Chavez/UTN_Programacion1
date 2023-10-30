# Función para comprobar si un número es múltiplo del otro
def is_multiple(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

# Solicitar dos números enteros al usuario
number1 = int(input("Ingrese el primer número entero: "))
number2 = int(input("Ingrese el segundo número entero: "))

# Comprobar si uno de los números es múltiplo del otro usando la función
if is_multiple(number1, number2):
    print(f"{number1} o {number2} es múltiplo del otro.")
else:
    print(f"{number1} y {number2} no son múltiplos entre sí.")