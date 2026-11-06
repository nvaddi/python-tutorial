class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def execute(self):
        super().work()

    def work(self):
        print("Developer writing code")

class Tester(Employee):
    def test(self):
        print("Tester is testing the code")

d = Developer()
d.execute()
# d.work()