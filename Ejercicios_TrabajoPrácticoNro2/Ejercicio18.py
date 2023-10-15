# Solicitar al usuario el total de horas trabajadas en el mes y el salario por hora.
horas_trabajadas = int(input("Ingrese el total de horas trabajadas: "))
salario_por_hora = float(input("Ingrese su salario por hora: "))

# Definir una constante para las horas laborales estándar
HORAS_ESTANDAR = 48

# Calcular el salario total
salario_total = horas_trabajadas * salario_por_hora

# Verificar si se trabajaron horas extras y calcular el salario correspondiente
if horas_trabajadas > HORAS_ESTANDAR:
    horas_extras = horas_trabajadas - HORAS_ESTANDAR
    salario_horas_extras = salario_por_hora * 1.1  # 10% más que las horas estándar
    salario_total += horas_extras * salario_horas_extras

# Mostrar el salario total
print(f"Su salario total es de: ${salario_total}")
