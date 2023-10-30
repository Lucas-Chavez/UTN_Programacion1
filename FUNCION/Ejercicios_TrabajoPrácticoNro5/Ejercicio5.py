# Definición de una función para calcular la temperatura media.
def calculate_mean_temperature(temperatures):
    # Suma de todas las temperaturas en la lista.
    sum_temperatures = sum(temperatures)
    # Número de días, que es igual a la cantidad de temperaturas en la lista.
    number_of_days = len(temperatures)
    # Cálculo de la temperatura media como la división entera de la suma entre el número de días.
    return sum_temperatures // number_of_days

# Solicitar al usuario la cantidad de días.
days_entry = int(input("Ingrese la cantidad de días: "))
# Lista para almacenar las temperaturas medias de cada día.
temperature_list = []

# Iterar sobre cada día para solicitar las temperaturas máximas y mínimas.
for days in range(days_entry):
    maximum_temperature = int(input(f"Ingrese la temperatura máxima del día {days + 1}: "))
    minimum_temperature = int(input(f"Ingrese la temperatura mínima del día {days + 1}: "))
    # Calcular la temperatura media como el promedio de la temperatura máxima y mínima.
    medium_temperature = (maximum_temperature + minimum_temperature) // 2
    # Agregar la temperatura media a la lista.
    temperature_list.append(medium_temperature)

# Calcular la temperatura media total llamando a la función.
average_total_temperature = calculate_mean_temperature(temperature_list)

# Mostrar la temperatura media total.
print(f"La temperatura media de los días ingresados es: {average_total_temperature}")



