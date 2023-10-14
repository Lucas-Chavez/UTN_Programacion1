# Solicita al usuario el valor del cateto adyacente del triángulo y lo almacena como un número de punto flotante.
cateto_adyacente = float(input("Digite el cateto adyacente del triángulo: "))
# Solicita al usuario el valor del cateto opuesto del triángulo y lo almacena como un número de punto flotante.
cateto_opuesto = float(input("Digite el cateto opuesto del triángulo: "))
# Calcula la hipotenusa del triángulo utilizando el teorema de Pitágoras.
hipotenusa = (cateto_adyacente**2 + cateto_opuesto**2) ** (1 / 2)
# Imprime el valor de la hipotenusa con dos decimales.
print(f"El valor de la hipotenusa del triángulo es de: {hipotenusa:.2f}")