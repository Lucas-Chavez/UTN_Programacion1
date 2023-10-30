import Ejercicio1
import Ejercicio2

# Bucle para ingresar socios
while True:
    username = input("Ingrese el nombre completo del socio (nombre apellido): ")
    # Salir del bucle si se ingresa un nombre vacío
    if username == "":
        break
    # Dividir el nombre en palabras
    word = username.split()
    # Validar que se ingresaron al menos nombre y apellido
    if len(word) < 2:
        print("Por favor, ingrese al menos nombre y apellido.")
        continue
    # Validar el DNI
    while True:
        number_dni = input("Ingrese el número de DNI del socio: ")
        if Ejercicio1.validate_dni(number_dni):
            break
        else:
            print("DNI inválido. Debe tener 7 u 8 dígitos.")
    
    # Identificador
    # Tomar la longitud el apellido (última palabra)
    last_name_length = str(Ejercicio2.last_word_length(username))
    # Tomar el primer nombre
    first_name = word[0]
    # Crear el identificador
    identifier = first_name + last_name_length + number_dni[:3]

    #Mostrar identificador
    print("\nIdentificador")
    print("Nombre: ", username)
    print("DNI: ", number_dni)
    print("ID ->", identifier)
    print("")