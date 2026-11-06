# Without encapsulation
# Bank - 1000
# Deposit - Money
# Show Balance

class Bank:
    def __init__(self):
        self.balance =  2000

    def deposit(self,amout):
        self.balance += amout

    def show_balance(self):
        print(self.balance)

    def withdraw(self,amout):
        self.balance -= amout

    def interest_calculate(self):
        self.interest = (self.balance * 2 * 2)/100
        self.balance+=self.interest
        print("with interest ",self.balance)

b = Bank()
b.deposit(200)
b.show_balance()
b.withdraw(200)
b.show_balance()
b.interest_calculate()
b.balance=0
b.show_balance()