class Account:
    def __init__(self, holder, balance=0.0):
        # Constructor de la clase con titular y saldo
        self.holder = holder
        self.balance = balance

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, holder):
        # Setter del titular (usamos un atributo privado)
        self._holder = holder

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            # Setter del saldo con validación
            self._balance = balance
        else:
            print("El saldo no puede ser negativo. No se realizaron cambios.")  # Validamos que el saldo no sea negativo

    def display(self):
        # Método para mostrar información de la cuenta
        print("Información de la Cuenta:")
        print(f"Titular: {self.holder}")  # Mostramos el titular
        print(f"Saldo: ${self.balance:.2f}")  # Mostramos el saldo con formato monetario

    def deposit(self, amount):
        if amount > 0:
            # Método para depositar dinero en la cuenta
            self.balance += amount
            print(f"${amount:.2f} depositados en la cuenta.")  # Mostramos el monto depositado
        else:
            print("El monto a depositar debe ser positivo. No se realizaron cambios.")  # Validamos el depósito

    def withdraw(self, amount):
        # Método para retirar dinero de la cuenta
        self.balance -= amount
        print(f"${amount:.2f} retirados de la cuenta.")  # Mostramos el monto retirado

client1 = Account(holder="Lucas Chavez", balance=2000.0)
client1.display()  # Mostramos la información de la cuenta
client1.deposit(500.0)  # Realizamos un depósito
client1.display()  # Mostramos la información actualizada
client1.withdraw(300.0)  # Realizamos un retiro
client1.display()  # Mostramos la información actualizada

