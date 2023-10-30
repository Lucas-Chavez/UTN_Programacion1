import validar

# Uso de la función para obtener un número entero positivo
mensaje = "Ingrese su edad: "
edad_usuarios = validar.entero_positivo(mensaje)
# Ahora que tenemos la edad como un número entero válido, mostramos los años cumplidos
for anio in range(1, edad_usuarios):
    print(anio)
    