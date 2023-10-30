# Almacena la contraseña en una variable
contrasena_usuario = "tu_contrasena_secreta"

while True:
    # Solicita al usuario que ingrese la contraseña
    input_contrasena = input("Ingrese la contraseña: ")
    
    # Compara la contraseña ingresada con la contraseña almacenada
    if input_contrasena == contrasena_usuario:
        print("La contraseña ingresada es correcta")
        break  # Sal del bucle si la contraseña es correcta
    else:
        print("La contraseña ingresada es incorrecta")