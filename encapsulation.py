# Encapsulation:

class Bank:
    def __init__(self):
        self.__balance= 1000 # __balance is now private, can be accessible with class only  

    def deposit(self, amount):
        self.__balance+= amount
        print("Total balance ", self.__balance)

    def showbalance(self):
        print("current balance: ",self.__balance)

    def withdraw(self, amount):
        self.__balance -= amount
        self.showbalance()

b = Bank()
b.showbalance()
b.__balance = 0
b.showbalance()
b.deposit(100)
b.withdraw(400)