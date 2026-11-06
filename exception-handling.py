# Exception handling (try- except)
# Exception handling is used to handle runtime errors without stopping the program 

try:
    val = int(input("Enter a number: "))
    print("Given input value is ",val)
    x = 10/val
    print("Result: ",x)
except ZeroDivisionError :
    print("Can't be divided by zero(0) value")    
else:
    name = input("Enter your name: ")
    print("No errors")
finally:
    print("Finally block executed")
