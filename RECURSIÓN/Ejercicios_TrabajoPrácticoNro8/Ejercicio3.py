def find_positions(a, b, start=0, positions=None):
    if positions is None:
        positions = []

    # Busca la siguiente ocurrencia de b en a a partir de la posición start
    pos = a.find(b, start)

    if pos != -1:
        positions.append(pos)
        # Llama a la función recursivamente para buscar más ocurrencias
        find_positions(a, b, pos + 1, positions)

    return positions

# Ejemplo de uso
a = "Un tete a tete con Tete"
b = "te"

result = find_positions(a, b)
print(f"Posiciones de '{b}' en '{a}':", result)