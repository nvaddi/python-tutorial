# Set in python - Unordered collection without duplicates using {}
# Set Operations - add, remove, discard, clear, union, intersection, difference

my_set = {10,20,30,10,40}
print("my set ", my_set)

#add()
my_set.add(35)
print("my set with add() ", my_set)

#remove()
my_set.remove(20)  # It removes the element, if element is not there it will throw any error
print("my set with remove() ", my_set)

#discard
my_set.discard(50) # It removes the element, if element is not there it won't throw any error

print("my set with discard() ", my_set)

a_set = {1,2}
b_set = {2,3}

c_set = a_set.union(b_set)
print("union ", c_set)

c_set = a_set.intersection(b_set)
print("intersection ", c_set) #common values in both sets

c_set = a_set.difference(b_set)
print("difference ", c_set) #shows the difference from both sets

