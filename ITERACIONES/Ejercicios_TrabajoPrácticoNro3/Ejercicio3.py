import validar

mensaje = "Digite un número entero positivo: "
numero_entrada = validar.entero_positivo(mensaje)
# Ahora que tenemos el número de entrada como un entero válido, mostramos los números impares
impares = [str(i) for i in range(1, numero_entrada) if i % 2 != 0]
resultado = ", ".join(impares)  # Unimos los números impares en una cadena separada por comas
print(f"Números impares desde 1 hasta {numero_entrada - 1} son: {resultado}")