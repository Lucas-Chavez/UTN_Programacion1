from random import sample, choice

# Función para extraer una bola de bingo aleatoria que no se haya extraído antes
def extract_random_ball(used_balls):
    # Generar una lista de bolas disponibles que no se han extraído
    available_balls = [number for number in range(1, 76) if number not in used_balls]
    
    if available_balls:
        # Elegir una bola aleatoria de las disponibles
        ball = choice(available_balls)
        used_balls.append(ball)  # Agregar la bola a la lista de bolas utilizadas
        return ball
    else:
        return None  # Devolver None si no hay bolas disponibles

from random import sample

# Función para generar un cartón de bingo
def generate_bingo_card():
    # Genera un cartón de bingo con 25 números únicos en el rango de 1 a 75
    # Utiliza una lista de comprensión para generar las filas del cartón
    # Se generan 5 filas, cada una con 5 números únicos
    return [sample(range(1, 76), 5) for _ in range(5)]

# Función para imprimir el cartón de Bingo
def display_bingo_card(cardboard):
    # Encabezado del cartón de Bingo
    print("\n----- Cartón de Bingo -----\n")
    print(f"{'B':<5} {'I':<5} {'N':<5} {'G':<5} {'O':<5} \n")

    for row in cardboard:
        display_bingo = ""  # Inicializa una cadena para mostrar los números de la fila
        for number in row:
            display_bingo += f"{number:<5} "  # Agrega cada número a la cadena, alineado a la izquierda
        print(display_bingo)  # Muestra la fila del cartón
        print()  # Salta a una nueva línea después de cada fila


# Función para verificar si hay una fila completa en el cartón de Bingo
def check_bingo_win(bingo_card):
    # Verifica si el jugador ganó con una línea completa
    for row in bingo_card:
        if all(number == "XX" for number in row):
            return True  # Devuelve True si una fila completa tiene "XX"
    
    # Verifica si el jugador ganó con una columna completa
    for col in range(5):
        if all(bingo_card[row][col] == "XX" for row in range(5)):
            return True  # Devuelve True si una columna completa tiene "XX"
    
    # Verifica si el jugador ganó con una diagonal completa de izquierda a derecha
    if all(bingo_card[i][i] == "XX" for i in range(5)):
        return True  # Devuelve True si la diagonal izquierda a derecha tiene "XX"
    
    # Verifica si el jugador ganó con una diagonal completa de derecha a izquierda
    if all(bingo_card[i][4-i] == "XX" for i in range(5)):
        return True  # Devuelve True si la diagonal derecha a izquierda tiene "XX"
    
    return False  # Devuelve False si no se ha ganado todavía


# Mensaje de bienvenida
print("¡Bienvenido al juego de Bingo personalizado!")

while True:
    used_balls = []  # Lista para rastrear los números seleccionados
    
    # Genera el cartón de Bingo del usuario y lo muestra
    input("Presiona Enter para generar tu cartón de Bingo...")
    user_bingo_card = generate_bingo_card()
    display_bingo_card(user_bingo_card)

    while True:
        input("Presiona Enter para extraer una bola de Bingo...")
        ball = extract_random_ball(used_balls)

        # Verifica si se han extraído todas las bolas
        if len(used_balls) == 75:
            print("Se han extraído todas las bolas. ¡Es un empate!")
            break
        print("Bola extraída:", ball)

        # Marca el número en el cartón del usuario como "XX" si se encuentra
        for row in user_bingo_card:
            if ball in row:
                row[row.index(ball)] = "XX" # reemplaza el elemento en la fila en la matriz
                display_bingo_card(user_bingo_card)  # Muestra el cartón actualizado
                break  # Sale del bucle si se encuentra el número en la fila

        # Verifica si el usuario ha ganado
        if check_bingo_win(user_bingo_card):
            print("¡Bingo! ¡Has ganado!\n")
            break

    play_again = input("¿Quieres jugar de nuevo? (S/N): ").strip().lower()
    if play_again != "s":
        print("Gracias por jugar al Bingo personalizado. ¡Hasta la próxima!")
        break