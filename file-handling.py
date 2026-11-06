#File handling 
# open() - to open a file
# "w" mode is used to write data to the file
# "r" mode is used to read data from the file
# "a" mode is used to add/append data to the file
# close() is used to close the file

# Writing data into a file
# file = open("data.txt","w")
# file.write("Welcome to python file handling programming")
# file.close()

# Reading data from a file
# file = open("data.txt","r")
# print("Reading file content: ",file.read())

# Appending data to a file
file = open("data.txt","a")
file.write(" successfully completed")

# Reading data from a file
file = open("data.txt","r")
print("File content ", file.read())
# Closing file
file.close()
