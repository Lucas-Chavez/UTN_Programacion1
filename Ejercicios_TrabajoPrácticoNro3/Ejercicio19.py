import validar

# Ingresar la cantidad de dinero que se desea ahorrar
# Llamamos a la función para obtener un número positivo
total_ahorros = validar.flotante_positivo("Ingrese la cantidad de dinero que desea ahorrar: ")  

# Inicializamos una variable para llevar un seguimiento de los ahorros acumulados
acumular_ahorros = 0

# Mientras los ahorros acumulados sean menores que el total deseado
while acumular_ahorros < total_ahorros:
    mensaje = f"Ingrese los ahorros que desea agregar a la alcancía (hasta ${total_ahorros - acumular_ahorros}): "
    ahorros = validar.flotante_positivo(mensaje)  # Solicitamos ahorros adicionales
    acumular_ahorros += ahorros  # Sumamos los ahorros a la cantidad acumulada

# Mostramos el total de ahorros acumulados al usuario
print(f"Usted ha acumulado un total de ${acumular_ahorros} en ahorros.")
