import validar

# Solicita al usuario que ingrese un número entero
entrada = validar.entero_positivo("Ingrese un número entero: ")
divisores = 0
# Solo necesitas verificar los divisores hasta la mitad del número
for i in range(1, entrada // 2 + 1):
    if entrada % i == 0:
        divisores += 1
    if divisores > 1:
        break
# Un número primo solo debe tener 2 divisores 
if divisores == 1:
    print(f"El número {entrada} es primo")
else:
    print(f"El número {entrada} no es primo")