# Inicializamos las variables para los dos primeros números de la secuencia
a = 0
b = 1
# Creamos un bucle for para generar y mostrar los números de Fibonacci
for i in range(11):
    print(a, end=" ")  # Imprimimos el valor actual de 'a' seguido de una coma y un espacio
    # Calculamos los siguientes dos números de la secuencia
    temp = a
    a = b
    b = temp + b