# Implement a program that simulates a basic bank account using BankAccount class:
class BankAccount:
    # We define methods with each of the actions that we can perform in our bank account.
    def __init__(self, cash):
        self.cash = cash
        self.movimiento = {}
    def withdrawal(self, amount):
        self.check_amount(amount)
        self.cash = self.cash - amount
        self.add_movement(-amount)

    def check_amount(self, amount):
        if amount < 0:
            raise ValueError("amount must be a positive number")
    def deposit(self, amount):
        self.check_amount(amount)
        self.cash = self.cash + amount
        self.add_movement(amount)

    def add_movement(self, amount):
        if len(self.movimiento) == 0:
            self.movimiento[1] = amount
        else:
            #We take the highest key and add 1
            new_key = max(self.movimiento.keys())
            self.movimiento[new_key + 1] = amount
    @property
    def current_balance(self):
        return self.cash


