#List Operations: change, append, remove, pop, clear
numbers = [10,20,30,40]

#Change
numbers[0] = 100
print("After assign elements: ", numbers)

#Append
numbers.append(50)
numbers.append(5)
numbers.append(60) 
print("After append ", numbers)

#Remove
numbers.remove(20) #using list value
#numbers.pop(2) #using list index 
print("After remove ", numbers)

#Assign at particular index
numbers[1] = 150
print("After assignment ", numbers)

