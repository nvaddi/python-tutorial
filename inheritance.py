#Inheritance

class Employee:
    def work(self):
        print("Employe is working")

class Developer(Employee):
    def code(self):
        print("Developer is coding")

class Tester(Employee):
    def test(self):
        print("Tester is testing the code")

dev = Developer()
dev.work()

t = Tester()
t.work()
t.test()