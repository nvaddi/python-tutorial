from abc import ABC, abstractmethod

class ATM:
    @abstractmethod
    def withdraw(self):
        pass
class SBI(ATM):
    def withdraw(self):
        print("Money withdrawn from SBI ATM")

class HDFC(ATM):
    def withdraw(self):
        print("Money withdrawn from HDFC")

atm1 = SBI()
atm2 = HDFC()

atm1.withdraw()
atm2.withdraw()