# Crear conjuntos para almacenar los nombres de los alumnos de nivel primario y secundario
primary = set()
secondary = set()

# Solicitar nombres de alumnos de nivel primario
print("Ingrese los nombres de los alumnos de nivel primario (ingrese 'x' para finalizar):")
while True:
    name_primary  = input()
    if name_primary  == 'x':
        break
    primary.add(name_primary )

# Solicitar nombres de alumnos de nivel secundario
print("Ingrese los nombres de los alumnos de nivel secundario (ingrese 'x' para finalizar):")
while True:
    name_secondary  = input()
    if name_secondary  == 'x':
        break
    secondary.add(name_secondary )

# Mostrar los nombres de todos los alumnos de nivel primario y secundario sin repeticiones
all_students  = primary.union(secondary)
print("\nNombres de todos los alumnos (sin repeticiones):")
for names in all_students :
    print(names)

# Encontrar los nombres que se repiten entre nivel primario y secundario
Names = primary.intersection(secondary)
print("\nNombres que se repiten entre nivel primario y secundario:")
for names in Names:
    print(names)

# Encontrar los nombres de nivel primario que no se repiten en nivel secundario
primary_names_not_repeated  = primary.difference(secondary)
print("\nNombres de nivel primario que no se repiten en nivel secundario:")
for name in primary_names_not_repeated :
    print(name)
