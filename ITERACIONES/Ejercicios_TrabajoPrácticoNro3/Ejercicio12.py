# Solicitar al usuario que ingrese una frase
frase = input("Ingrese una frase: ")
# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ")
# Utilizar el método count() para contar las ocurrencias de 'letra' en 'frase'
contador_letras = frase.count(letra)
# Mostrar el resultado al usuario
print(f"La letra '{letra}' aparece un total de {contador_letras} vez en la frase: '{frase}'")