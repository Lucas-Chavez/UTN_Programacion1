def login(username, password, attempts):
    # Definición de las credenciales correctas
    correct_username = "usuario1"
    correct_password = "asdasd"

    # Comprueba si el usuario y la contraseña coinciden con los valores correctos
    if username == correct_username and password == correct_password:
        return True, attempts  # Devuelve True si el inicio de sesión es exitoso
    else:
        return False, attempts + 1  # Devuelve False y aumenta el contador de intentos fallidos

# Número máximo de intentos permitidos
max_attempts = 3
attempts = 0
logged_in = False  # Inicialmente, no se ha iniciado sesión

# Mientras el número de intentos sea menor que el máximo y no se haya iniciado sesión
while attempts < max_attempts and not logged_in:
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    logged_in, attempts = login(username, password, attempts)  # Intento de inicio de sesión

    if logged_in:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")

# Comprobar si se ha agotado el número de intentos
if not logged_in:
    print("Se han agotado los intentos.")

