import validar

# Llamamos a la función para solicitar un número entero positivo
cantidad_ciclos = validar.entero_positivo("cuántos números desea introducir: ")
# Inicializamos el contador de números negativos a 0
contador_negativos = 0
# Iteramos a través de las repeticiones especificadas por el usuario
for i in range(cantidad_ciclos):
    # Solicitamos al usuario que ingrese un número y manejamos errores de valor no válido
    entrada = validar.entrada_flotante(f"\nN°{i + 1}: Ingrese un número: ")
    # Comprobamos si el número ingresado es negativo
    if entrada < 0:
        contador_negativos += 1  # Si es negativo, incrementamos el contador
# Mostramos la cantidad de números negativos introducidos por el usuario
print(f"\nSe han introducido {contador_negativos} números negativos.")