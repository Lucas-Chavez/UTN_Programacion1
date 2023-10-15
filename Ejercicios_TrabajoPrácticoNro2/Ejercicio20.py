# Solicitar al usuario que ingrese las cuatro notas.
primer_nota = float(input("Ingrese su primera nota: "))
segunda_nota = float(input("Ingrese su segunda nota: "))
tercer_nota = float(input("Ingrese su tercera nota: "))
cuarta_nota = float(input("Ingrese su cuarta nota: "))

# Calcular el promedio de las notas.
promedio_notas = (primer_nota + segunda_nota + tercer_nota + cuarta_nota) / 4

# Comprobar si el promedio es mayor o igual a 6 para determinar si el alumno aprueba o reprueba.
if promedio_notas >= 6:
    print(f"Felicidades, has aprobado con un promedio de {promedio_notas:.2f}")
else:
    print(f"Lo siento, has desaprobado con un promedio de {promedio_notas:.2f}")
