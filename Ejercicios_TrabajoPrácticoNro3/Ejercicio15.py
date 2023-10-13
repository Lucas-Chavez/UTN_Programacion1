import validar

# Llamamos a la función para solicitar un número entero positivo
mensaje = "Digite un número entero positivo: "
numero = validar.entero_positivo(mensaje)
print(f"Los divisores de {numero} son:")
# Verificamos si el número ingresado es cero, si lo es, mostramos un mensaje
if numero == 0:
    print("El número 0 no tiene divisores ya que es indefinido.")
else:
    # Iteramos a través de los números desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)  # Si el número es divisible por 'i', lo mostramos como divisor