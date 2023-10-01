try:
    # Solicitar al usuario ingresar la fecha en formato "día, DD/MM"
    fecha = input("Ingrese la fecha actual en formato \"día, DD/MM\": ")

    # Dividir la entrada en las partes correspondientes utilizando la coma como delimitador
    dia, resto = fecha.split(", ")

    # Luego, dividir 'resto' en las partes correspondientes utilizando la barra diagonal como delimitador
    dia_numero, mes_numero = resto.split("/")

    # Definir una lista de días de la semana
    lista_dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    # Validar si el día ingresado está en la lista de días y si los números de día y mes son válidos
    if (dia.lower() in lista_dias) and (1 <= int(dia_numero) <= 31) and (1 <= int(mes_numero) <= 12):
        # Realizar acciones específicas para diferentes días de la semana
        if dia.lower() in lista_dias[0:3]:
            # Caso: Día de Exámenes
            print(f"El día {dia.lower()} corresponde a \"Exámenes\".")
            # Solicitar la cantidad de alumnos aprobados y desaprobados
            alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
            total_alumnos = alumnos_aprobados + alumnos_desaprobados
            porcentaje_aprobados = (alumnos_aprobados / total_alumnos) * 100
            porcentaje_aprobados = round(porcentaje_aprobados, 2)  # Redondear a dos decimales
            print(f"El porcentaje de alumnos aprobados es de: {porcentaje_aprobados}%")
        elif dia.lower() in lista_dias[3:4]:
            # Caso: Día de Prácticas Habladas
            print(f"El día {dia.lower()} corresponde a \"Prácticas Habladas\".")
            # Solicitar el porcentaje de asistencias
            porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencias: "))
            mensaje = ("Asistió la mayoría" if porcentaje_asistencia > 50 else "No asistió la mayoría")
            print(mensaje)
        elif dia.lower() in lista_dias[4:5]:
            # Caso: Día de Inglés Para Viajeros
            print(f"El día {dia.lower()} corresponde a \"Inglés Para Viajeros\".")
            if int(dia_numero) == 1 and (int(mes_numero) == 1 or int(mes_numero) == 7):
                print("\"Comienzo de nuevo ciclo.\"")
                # Solicitar la cantidad de alumnos y el arancel por alumno
                cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
                arancel_alumno = float(input("Ingrese el arancel por cada alumno $"))
                ingreso_total = cantidad_alumnos * arancel_alumno
                print(f"El ingreso total es de ${ingreso_total}.")
            else: 
                print("No se requiere el ingreso de ningún dato")
        else:
            # Caso: Otros días de la semana
            print(f"El día {dia.lower()} no se dicta ninguna clase.")
    else:
        # Caso: Fecha no válida
        print("La fecha ingresada no es válida.")
except ValueError:
    # Caso: Error de formato de entrada
    print("La entrada no tiene el formato esperado.")