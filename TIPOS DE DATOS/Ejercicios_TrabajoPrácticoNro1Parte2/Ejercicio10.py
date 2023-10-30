# Obtener las tres calificaciones parciales
calificacion_parcial1 = float(input("Ingrese la calificación del Parcial 1: "))
calificacion_parcial2 = float(input("Ingrese la calificación del Parcial 2: "))
calificacion_parcial3 = float(input("Ingrese la calificación del Parcial 3: "))

# Calcular el promedio de las calificaciones de los parciales
promedio_parciales = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3

# Obtener la calificación del examen final
calificacion_examen_final = float(input("Ingrese la calificación del Examen Final: "))

# Obtener la calificación del trabajo final
calificacion_trabajo_final = float(input("Ingrese la calificación del Trabajo Final: "))

# Calcular la calificación final
calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

# Mostrar la calificación final
print(f"La calificación final en la materia de Algoritmos es: {calificacion_final:.2f}")
