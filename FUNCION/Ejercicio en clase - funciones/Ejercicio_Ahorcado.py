import sys
# Agregamos una ubicación específica a sys.path para importar un módulo personalizado.
sys.path.append('C:/Users/chave/OneDrive/Escritorio/GIT-PROGRAMACION/FUNCION')
# Importamos el módulo "Funciones"
import Funciones

print("BIENVENIDO AL JUEGO DE AHORCADOS")
print("----------------------------------")
print("Reglas:")
print("Debe adivinar las letras de una palabra antes de quedarse sin vidas. Comencemos!")
print("----------------------------------")

# Se elige una palabra aleatoria.
word = Funciones.choose_word()

# Se inicializa el juego con la palabra elegida.
word, letter, guessed_letters, live_player = Funciones.initialize_game(word)

# Bucle principal del juego.
while live_player > 0:
    # Muestra el estado actual del juego.
    Funciones.display_status(letter, live_player)
    
    # Obtiene la letra ingresada por el usuario y realiza validaciones.
    add_letter = Funciones.get_user_input(guessed_letters)
    guessed_letters += add_letter

    if add_letter in word:
        print("La letra ingresada es correcta.")
        # Actualiza la palabra oculta con la letra adivinada.
        letter = Funciones.update_letter(word, letter, add_letter)
    else:
        print("La letra ingresada es incorrecta.")
        live_player -= 1

    if "_" not in letter:
        print("¡Felicidades! Ha adivinado la palabra:", " ".join(letter))
        break

if live_player == 0:
    print("¡Perdiste! La palabra era:", " ".join(word))