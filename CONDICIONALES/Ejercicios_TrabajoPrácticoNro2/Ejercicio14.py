# Solicitar al usuario los coeficientes de la ecuación (a y b)
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

# Verificar si la ecuación es de primer grado (a no puede ser 0)
if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones (todos los números son solución).")
    else:
        print("La ecuación no tiene solución (no es posible dividir por 0).")
else:
    # Calcular la solución de la ecuación usando la fórmula
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x}")
