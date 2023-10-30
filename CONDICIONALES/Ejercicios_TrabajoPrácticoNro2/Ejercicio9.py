# Definir el alfabeto español personalizado
import string

# Establecer la posición de la letra "Ñ" en el alfabeto español
posicion, letra = 14, "Ñ"

# Crear un alfabeto español personalizado con la letra "Ñ" en la posición deseada
alfabeto_espanol = (string.ascii_uppercase[:posicion] + letra + string.ascii_uppercase[posicion:])

# Solicitar al usuario que ingrese su nombre y sexo
nombre_alumno = input("Ingrese su nombre: ").strip().upper()
genero_alumno = input("Ingrese su sexo: ").strip().lower()

# Definir los grupos y las letras que determinan la pertenencia a cada grupo
grupo = {
    "femenino": ["Grupo A", (alfabeto_espanol[0:13])],
    "masculino": ["Grupo B", (alfabeto_espanol[13::])]
}

# Verificar si el género y la letra inicial del nombre corresponden a un grupo
if genero_alumno in grupo and nombre_alumno[0] in grupo[genero_alumno][1]:
    print(f"El alumno {nombre_alumno.capitalize()} de género {genero_alumno} pertenece al {grupo[genero_alumno][0]}")
else:
    print(f"No se ha podido identificar el grupo al que pertenece el alumno {nombre_alumno.capitalize()}")
