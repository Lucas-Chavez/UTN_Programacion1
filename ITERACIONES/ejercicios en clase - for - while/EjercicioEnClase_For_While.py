# EJERCICIO 1
# Función para cifrar un mensaje
def cifrado_mensaje(alfabeto, mensaje, desplazamiento):
    mensaje_cifrado = ("") # Inicializa una cadena vacía para almacenar el mensaje cifrado
    for e in mensaje:
        if e in alfabeto:  # Verifica si el carácter está en el alfabeto personalizado
            indice = alfabeto.index(e)  # Encuentra el índice del carácter en el alfabeto
            cifrado = alfabeto[(indice + desplazamiento) % len(alfabeto)]  # Aplica el desplazamiento
            mensaje_cifrado += cifrado  # Agrega el carácter cifrado al mensaje cifrado
        else:
            mensaje_cifrado += e  # Si el carácter no está en el alfabeto, lo agrega tal cual al mensaje cifrado
    return mensaje_cifrado  # Retorna el mensaje cifrado
import string
# Definir el alfabeto español personalizado
posicion, letra = 14, "Ñ"
alfabeto_espanol = (string.ascii_uppercase[:posicion] + letra + string.ascii_uppercase[posicion:])
# Solicitar la cantidad de desplazamiento por letra
while True:
    # Verificamos si la entrada es válida y es un número positivo
    try:
        cantidad_desplazamiento = input("Digite la cantidad de desplazamiento por letra: ")
        if int(cantidad_desplazamiento) < 0 if cantidad_desplazamiento.isdigit() else True:
            raise ValueError("Debe ingresar un número entero positivo.")
        cantidad_desplazamiento = int(cantidad_desplazamiento)
        break
    except ValueError as e:
        print(f"Error: {e}")
# Crear una lista para almacenar los mensajes cifrados
lista_cifrados = []
# Solicitar y cifrar los mensajes para 5 oficiales
for i in range(5):
    mensaje = input(f"Digite un mensaje para el oficial N°{i+1}: ")
    cifrado = cifrado_mensaje(alfabeto_espanol, mensaje.upper(), cantidad_desplazamiento)
    lista_cifrados.append(cifrado)
# Imprimir los mensajes cifrados
for i, cifrado in enumerate(lista_cifrados):
    print(f"Mensaje cifrado para oficial N°{i+1}: {cifrado}")


print("")  # Salto de Linea


# EJERCICIO 2
# Inicializamos una lista para almacenar los números ingresados
numero_ingresados = []
while True:
    try:
        # Solicitamos al usuario que ingrese un número
        entrada = input("Digite un numero entero positivo (Ingrese 0 para salir): ")
        # Verificamos si la entrada es válida y es un número positivo
        if int(entrada) < 0 if entrada.isdigit() else True:
            raise ValueError("Debe ingresar un número entero positivo.")
        entrada = int(entrada)
        # Si el número ingresado es 0, salimos del bucle
        if entrada == 0:
            break
        # Agregamos el número ingresado a la lista
        numero_ingresados.append(entrada)
    except ValueError as e:
        # Capturamos y manejamos la excepción si se ingresa un valor no válido
        print(f"Error: {e}")

# Inicializamos contadores para los dígitos pares e impares
contador_pares = 0
contador_impares = 0
total_pares = 0
total_impares = 0  
# Iteramos a través de los números ingresados
for numero in numero_ingresados:
    copia_numero = numero
    contador_pares = 0  # Reiniciamos el contador de dígitos pares en cada iteración
    contador_impares = 0  # Reiniciamos el contador de dígitos impares en cada iteración
    # Iteramos a través de los dígitos del número
    while copia_numero > 0:
        digito = copia_numero % 10
        # Verificamos si el dígito es par o impar y actualizamos los contadores
        if digito % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
        # Eliminamos el último dígito del número dividiendo entre 10
        copia_numero //= 10
    # Mostramos la cantidad de dígitos pares e impares en el número
    print(
        f"El número {numero} posee {contador_pares} dígitos pares y {contador_impares} dígitos impares"
    )
    # Actualizamos los totales de dígitos pares e impares
    total_pares += contador_pares
    total_impares += contador_impares
# Imprimimos el total de dígitos pares e impares al final
print(
    f"El total de dígitos pares es de {total_pares}\n"
    f"El total de dígitos impares es de {total_impares}"
)
