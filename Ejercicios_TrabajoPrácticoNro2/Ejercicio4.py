# Definir un diccionario con las opciones de los candidatos y sus partidos.
partido = {
    "A": "Partido Rojo",
    "B": "Partido Verdad",
    "C": "Partido Azul"
}

# Mostrar las opciones al usuario.
print(
    f"Seleccione el partido de un candidato. Opciones: (A, B, C)\n"
    f"Candidato A: {partido['A']}\n"
    f"Candidato B: {partido['B']}\n"
    f"Candidato C: {partido['C']}\n"
)

# Solicitar al usuario que seleccione una opción y limpiar espacios y convertirla a mayúsculas.
seleccion_candidato = input("Seleccione una opción: ").strip().upper()

# Validar si la opción seleccionada está en el diccionario de opciones.
if seleccion_candidato in partido:
    print(f"Usted ha votado por el {partido[seleccion_candidato]}")
else:
    print("Por favor, ingrese una opción válida (A, B o C).")