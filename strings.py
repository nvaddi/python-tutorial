# String methods help us to chage, search, format the text
# upper()
# lower()
# strip()
# replace()
# split()
# count()
# find()

text = input("Enter your text: ")
print("text.upper(): ",text.upper()) # converts the given text to uppercase
print("text.lower(): ",text.lower()) # converts the give text to lowercase

text1 = "   Vaddi   "
print("text.strip(): ",text.strip()) #removes additional spaces before and after

text2 = "I am going to picnic"
print("text.split(' ' ): ",text2.split(" ")) # based the given character (here space) it splits the text and return a list

text3 = "I am going to picnic"
print("text.count('i'): ",text3.count("i")) # getting the count of 'i' in the string

text4 = "I am going to Pune"
print("text.replace(Pune, Hyderabad): ",text4.replace("Pune","Hyderabad")) # replaces the Pune with Hyderabad


print("text.find(o): ",text4.find("o")) #returns first index of the 'o' of input string



