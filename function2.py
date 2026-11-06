# def test(name):
#     print("Hi ",name)

# test("Niranjan")    

def calc(a,b):
    return a+b, a-b, a*b

add,sub,mul=calc(20,5)
print(add, sub, mul)


list1 = [10,20,30]

def calc1(numbers):
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    
    
calc1(list1)