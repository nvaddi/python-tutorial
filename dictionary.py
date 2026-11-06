#Dictionary in python - key-value pair, mutable, unordered

#Example: {"name": "Niranjan Vaddi"}
         # name --> key
         # value --> Niranjan Vaddi
dict1 = {
    "firstName": "Niranjan",
    "lastName": "Vaddi",
    "age": 35,
    "company": "Capgemini",
    "city": "Hyderabad"
}

print(dict1["firstName"])

dict1["firstName"] = "Mithila Rani"
dict1["age"] = 5

print(dict1)

dict1["contact"] = "8467987690" #adding new property to dictionary
print(dict1)

dict1.pop("contact") # removing contact property
print(dict1)

dict1.popitem() #removes the last item of dictionary
print(dict1)

print(dict1.keys()) # returns only keys
print(dict1.values()) # returns only values

print(dict1.items()) #
