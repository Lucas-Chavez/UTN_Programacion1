# Solicitar al usuario que ingrese un día de la semana
dia_semana = input("Ingrese un día de la semana: ").strip().lower()

# Comparar el día ingresado con diferentes días de la semana y mostrar mensajes correspondientes
if dia_semana == "lunes":
    print("¡Es lunes! ¡Comienza una nueva semana!")
elif dia_semana == "viernes":
    print("¡Es viernes! ¡Casi llega el fin de semana!")
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("¡Es fin de semana! Disfruta tu tiempo libre.")
else:
    print("No es lunes, viernes, sábado ni domingo. Día normal de la semana.")
