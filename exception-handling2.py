try:
    val = int(input("Enter a number "))
    print("Division value: ",10/val)
except ZeroDivisionError:
    print("Can't divide with zero(0) value")

except ValueError:
    print("Enter valid number")

finally:
    print("Finally block executed")