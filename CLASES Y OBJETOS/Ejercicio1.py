class Person:
    def __init__(self, name='', age=0, dni=''):
        # Constructor de la clase que inicializa las propiedades.
        self.name = name
        self.age = age
        self.dni = dni

    # Propiedad 'name' con su getter y setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Propiedad 'age' con su getter y setter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("La edad no puede ser negativa. Se establecerá como 0.")
            self._age = 0

    # Propiedad 'dni' con su getter y setter
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    def display(self):
        # Método para mostrar la información de la persona.
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"DNI: {self.dni}")

    def isAdult(self):
        # Método que verifica si la persona es adulta (mayor o igual a 18 años).
        return self.age >= 18

person1 = Person(name="Lucas", age=19, dni="12345678")
person1.display()
if person1.isAdult():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")