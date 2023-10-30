# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")
# Rebanar la palabra en reversa y recorrer las letras
for letra in palabra[::-1]:
    print(letra)