# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calcular la raíz cuadrada y la raíz cúbica
raiz_cuadrada = numero**1/2 # La raíz cuadrada es equivalente a elevar el número a 1/2.
raiz_cubica = numero**1/3  # La raíz cúbica es equivalente a elevar el número a 1/3.

# Paso 3: Mostrar los resultados
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
print(f"La raíz cúbica de {numero} es {raiz_cubica}")