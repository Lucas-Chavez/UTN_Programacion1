import random

# Función para generar una matriz 10x10 con valores aleatorios del 0 al 9
def generate_matrix():
    # Inicializa una matriz de 10x10 con ceros
    matrix = [[0 for _ in range(10)] for _ in range(10)]

    # Llena la matriz con valores aleatorios del 0 al 9, asegurándose de que los valores en la diagonal sean 0
    for i in range(10):
        for j in range(10):
            if i != j:  # Asegura que los valores en la diagonal no sean modificados
                matrix[i][j] = random.randint(0, 9)

    return matrix


goals = generate_matrix()  # Genera una matriz de goles aleatoria

num_teams = len(goals)  # Obtiene el número de equipos, que es igual al tamaño de la matriz

# Listas para almacenar estadísticas de los equipos
wins = [0] * num_teams  # Almacena el número de triunfos para cada equipo
draws = [0] * num_teams  # Almacena el número de empates para cada equipo
losses = [0] * num_teams  # Almacena el número de derrotas para cada equipo
goals_scored = [0] * num_teams  # Almacena el número total de goles marcados por cada equipo
goals_received = [0] * num_teams  # Almacena el número total de goles recibidos por cada equipo
points = [0] * num_teams  # Almacena el número total de puntos obtenidos por cada equipo

# Calcular estadísticas para cada equipo
for team in range(num_teams):
    for opponent in range(num_teams):
        if team != opponent:  # Asegura que no se compare un equipo consigo mismo
            team_goals = goals[team][opponent]  # Obtiene los goles marcados por el equipo en el enfrentamiento
            opponent_goals = goals[opponent][team]  # Obtiene los goles marcados por el oponente en el enfrentamiento
            goals_scored[team] += team_goals  # Agrega los goles marcados por el equipo
            goals_received[team] += opponent_goals  # Agrega los goles recibidos por el equipo
            if team_goals > opponent_goals:
                wins[team] += 1  # Incrementa el número de triunfos si el equipo ganó
                points[team] += 3  # Agrega 3 puntos por el triunfo
            elif team_goals < opponent_goals:
                losses[team] += 1  # Incrementa el número de derrotas si el equipo perdió
            else:
                draws[team] += 1  # Incrementa el número de empates si fue un empate
                points[team] += 1  # Agrega 1 punto por el empate


# Muestra las estadísticas para cada equipo
for team in range(num_teams):
    print(f"Equipo {team + 1}:")
    print(f"Triunfos: {wins[team]}")
    print(f"Empates: {draws[team]}")
    print(f"Derrotas: {losses[team]}")
    print(f"Goles Marcados: {goals_scored[team]}")
    print(f"Goles Recibidos: {goals_received[team]}")
    print(f"Diferencia de Goles: {goals_scored[team] - goals_received[team]}")
    print(f"Puntos: {points[team]}\n")
