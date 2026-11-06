#__init__ is a special method (constructor)
#__init__ runs automatically when an object is created
# self stores data inside object
 
class Car:
    name="Tata Sierra"
    color="NavyBlue"

#special function/ constructor
    def __init__(self):
        print(self.name, self.color)

    def speed(self):
        print("speed() executed")

car = Car()
car.speed()