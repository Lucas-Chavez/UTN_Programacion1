import validar

# Uso de la función para obtener un número entero positivo
mensaje = "Digite un número entero positivo: "
numero_entrada = validar.entero_positivo(mensaje)
# Creamos una lista utilizando una comprensión de lista.
# Generamos una cuenta regresiva desde 'numero_entrada' hasta 0.
cuenta_atras = [str(i) for i in range(numero_entrada, -1, -1)]
# Unimos los números de la cuenta regresiva en una cadena separada por comas.
resultado = ", ".join(cuenta_atras)
# Mostramos la cuenta regresiva al usuario.
print(f"La cuenta atrás desde {numero_entrada} hasta 0 es: {resultado}")