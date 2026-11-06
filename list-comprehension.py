# List comprehension is a short way to create a list
# It uses one line instead of loop
# It makes code short and easy to read
# We can also add conditions inside it

#num_list = [1,2,3,4,5] #manual declaration

num_list = []

#Approach - 1
# for i in range(1,6):
#     num_list.append(i)
# print(num_list)

for i in range(1,11):
   if i % 2 == 0:
    num_list.append(i);
print("Even numbers ",num_list)

num_list.clear()

for i in range(1,11):
   if i % 2 != 0:
    num_list.append(i);
print("Odd numbers ",num_list)

num_list.clear()

#Approach - 2
num_list = [i for i in range(1,11) if i % 2 == 0]
print("Even numbers: ",num_list)

num_list = [i for i in range(1,11) if i % 2 == 1]
print("Odd numbers: ",num_list)