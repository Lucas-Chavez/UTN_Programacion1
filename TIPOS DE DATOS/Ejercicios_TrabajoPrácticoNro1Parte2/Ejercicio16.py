nombre_completo = input("Ingrese su nombre y apellidos (nombre seguido de dos apellidos): ")
nombres = nombre_completo.split()

# Verificamos que se hayan proporcionado al menos 3 partes (nombre, primer apellido, segundo apellido)
if len(nombres) == 3:
    nombre = nombres[0]
    primer_apellido = nombres[1]
    segundo_apellido = nombres[2]
    iniciales = f"Inicial del nombre {nombre}: {nombre[0]}\n"
    iniciales += f"Inicial del primer apellido {primer_apellido}: {primer_apellido[0]}\n"
    iniciales += f"Inicial del segundo apellido {segundo_apellido}: {segundo_apellido[0]}\n"
    print(iniciales)
else:
    print("Debe ingresar un nombre y dos apellidos separados por espacios.")
