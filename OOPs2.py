# self means current class object
# It connects to the class

class Employee:
    def employeeDetails(self, name, address):
        print(self)
        print("Hello employee ",name, address)

emp = Employee()
print(emp)
emp.employeeDetails("Niranjan", "Hyderabad")