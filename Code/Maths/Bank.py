# Implement a program that simulates a basic bank account using BankAccount class:
class BankAccount:
    def __init__(self, cash, income, bill):
        self.money = cash
        self.income = income
        self.bill = bill

    @property
    def balance(self):
        return self.money, self.income, self.bill
