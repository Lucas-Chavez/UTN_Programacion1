# Funciones utilizadas en ejercicio "Ejercicio_en_clase _Funciones"
# Función para sumar los digitos de un número
def add_digits(number):
    add = 0
    while number > 0:
        digit = number % 10  # Obtenemos el último dígito.
        add += digit  # Sumamos el dígito a la suma.
        number //= 10  # Eliminamos el último dígito.
    return add

# Función para sumar los números en una lista
def addition_number(list_numbers):
    # Sumamos todos los números en la lista y devolvemos el resultado
    addition = sum(list_numbers)
    return addition

# Funciones utilizadas en ejercicio "Ejercicio_Ahorcado"
# Función para elegir una palabra aleatoria del conjunto de palabras.
def choose_word():
    import random
    list_words = ["codigo", "bug", "lenguaje", "lista", "tupla", "vector", "matriz", "diccionario"]
    return random.choice(list_words)

# Función para inicializar el juego con la palabra elegida.
def initialize_game(word):
    length = len(word)
    letter = "_" * length  # Inicializa la palabra a adivinar con guiones bajos.
    guessed_letters = ""  # Inicializa la lista de letras adivinadas.
    live_player = 6  # Inicializa el número de vidas.
    return word, letter, guessed_letters, live_player

# Función para mostrar el estado actual del juego.
def display_status(letter, live_player):
    print("Palabra a adivinar:", " ".join(letter))
    print(f"Vidas restantes: {live_player}")

# Función para obtener la entrada del usuario.
def get_user_input(guessed_letters):
    while True:
        add_letter = input("Ingrese una letra: ").lower()
        if len(add_letter) != 1 or not add_letter.isalpha():
            print("Por favor, ingrese una sola letra válida.")
        elif add_letter in guessed_letters:
            print("Ya ha intentado con esa letra.")
        else:
            return add_letter

# Función para actualizar la palabra a adivinar con las letras adivinadas.
def update_letter(word, letter, add_letter):
    new_letter = ""
    for i in range(len(word)):
        if add_letter == word[i]:
            new_letter += add_letter
        else:
            new_letter += letter[i]
    return new_letter
