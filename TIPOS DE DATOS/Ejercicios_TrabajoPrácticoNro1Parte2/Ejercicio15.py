# Solicitar al usuario la hora de partida y el tiempo de viaje en segundos
HH_partida = int(input("Ingrese la hora de partida (HH): "))
MM_partida = int(input("Ingrese los minutos de partida (MM): "))
SS_partida = int(input("Ingrese los segundos de partida (SS): "))
T_viaje = int(input("Ingrese el tiempo de viaje en segundos (T): "))

# Calcular la hora de llegada
tiempo_partida_segundos = HH_partida * 3600 + MM_partida * 60 + SS_partida
tiempo_llegada_segundos = tiempo_partida_segundos + T_viaje

# Convertir el tiempo de llegada a horas, minutos y segundos
HH_llegada = tiempo_llegada_segundos // 3600
MM_llegada = (tiempo_llegada_segundos % 3600) // 60
SS_llegada = tiempo_llegada_segundos % 60

# Mostrar la hora de llegada a la ciudad B
print(f"Hora de llegada a la ciudad B: {HH_llegada:0>2}:{MM_llegada:0>2}:{SS_llegada:0>2}")
