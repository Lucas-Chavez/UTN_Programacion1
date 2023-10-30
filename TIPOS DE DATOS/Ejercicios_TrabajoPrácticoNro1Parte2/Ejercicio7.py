minutos_entrada = int(input("Digite la cantidad de minutos: "))
# Calcula las horas dividiendo los minutos por 60 y redondea al número entero más cercano.
horas = minutos_entrada // 60
# Calcula los minutos restantes utilizando el operador módulo (%).
minutos = minutos_entrada % 60
# Imprime el resultado.
print(f"{minutos_entrada} minutos son: {horas} horas y {minutos} minutos")