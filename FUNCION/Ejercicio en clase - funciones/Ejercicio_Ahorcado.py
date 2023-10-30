import random

def choose_word(word_list):
    # Elige una palabra aleatoria de la lista de palabras
    return random.choice(word_list)

def initialize_game(word):
    # Inicializa el juego con la palabra elegida
    # Inicializa la palabra oculta y otras variables del juego
    letter = ["_" for _ in word]
    guessed_letters = ""
    live_player = 6  # Cantidad de vidas
    return word, letter, guessed_letters, live_player

def display_status(letter, live_player):
    # Muestra el estado actual del juego, la palabra oculta y las vidas restantes
    print("Palabra:", " ".join(letter))
    print("Vidas restantes:", live_player)

def get_user_input(guessed_letters):
    # Obtiene la letra ingresada por el usuario y realiza validaciones
    while True:
        add_letter = input("Ingresa una letra: ").lower()
        if len(add_letter) != 1:
            print("Por favor, ingresa una sola letra.")
        elif not add_letter.isalpha():
            print("Por favor, ingresa una letra válida.")
        elif add_letter in guessed_letters:
            print("Ya has ingresado esa letra. Intenta con otra.")
        else:
            return add_letter

def update_letter(word, letter, add_letter):
    # Actualiza la palabra oculta con la letra adivinada
    for i, char in enumerate(word):
        if char == add_letter:
            letter[i] = add_letter
    return letter

# Lista de palabras posibles
word_list = ["python", "java", "javascript", "html", "css", "ruby", "csharp", "php"]

print("BIENVENIDO AL JUEGO DE AHORCADOS")
print("----------------------------------")
print("Reglas:")
print("Debe adivinar las letras de una palabra antes de quedarse sin vidas. Comencemos!")
print("----------------------------------")

# Se elige una palabra aleatoria.
word = choose_word(word_list)

# Se inicializa el juego con la palabra elegida.
word, letter, guessed_letters, live_player = initialize_game(word)

# Bucle principal del juego.
while live_player > 0:
    # Muestra el estado actual del juego.
    display_status(letter, live_player)
    
    # Obtiene la letra ingresada por el usuario y realiza validaciones.
    add_letter = get_user_input(guessed_letters)
    guessed_letters += add_letter

    if add_letter in word:
        print("La letra ingresada es correcta.")
        # Actualiza la palabra oculta con la letra adivinada.
        letter = update_letter(word, letter, add_letter)
    else:
        print("La letra ingresada es incorrecta.")
        live_player -= 1

    if "_" not in letter:
        print("¡Felicidades! Ha adivinado la palabra:", " ".join(letter))
        break

if live_player == 0:
    print("¡Perdiste! La palabra era:", " ".join(word))