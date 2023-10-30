# Solicitar al usuario que ingrese su nombre de usuario y contraseña
usuario = input("Ingrese su nombre de usuario: ")
contrasenia = input("Ingrese su contraseña: ")

# Comprobar si el nombre de usuario es "Gwenevere"
usuario_valido = usuario == "Gwenevere"

# Comprobar si la contraseña es "excalibur"
contrasenia_valida = contrasenia == "excalibur"

# Verificar si tanto el nombre de usuario como la contraseña son correctos
if usuario_valido and contrasenia_valida:
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado")
