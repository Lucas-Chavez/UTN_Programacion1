# Definición de la clase Triangle (Triángulo)
class Triangle:
    # Constructor de la clase con tres lados (side1, side2, side3)
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Método para determinar el tipo de triángulo (equilátero, isósceles o escaleno)
    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "equilátero" # Todos los lados son iguales
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "isósceles" # Dos lados son iguales
        else:
            return "escaleno" # Todos los lados son diferentes

    # Método para obtener el lado más largo del triángulo
    def get_largest_side(self):
        return max(self.side1, self.side2, self.side3)

# Función para ingresar los datos de un triángulo desde el usuario
def input_triangle():
    side1 = float(input("Ingrese la longitud del primer lado: ")) # Ingresar longitud del primer lado
    side2 = float(input("Ingrese la longitud del segundo lado: ")) # Ingresar longitud del segundo lado
    side3 = float(input("Ingrese la longitud del tercer lado: "))  # Ingresar longitud del tercer lado

    return Triangle(side1, side2, side3)  # Devuelve un objeto Triangle con los lados ingresados

# Llamada a la función para ingresar datos y crear un objeto Triangle
triangle = input_triangle()

# Determinar el tipo del triángulo y el lado más largo
type = triangle.determine_type()
largest_side = triangle.get_largest_side()

# Mostrar el tipo de triángulo y el lado más largo
print(f"El triángulo es de tipo {type}.")
print(f"El lado con mayor longitud es de {largest_side} unidades.")
