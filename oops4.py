class Car:
    wheels = 4
    steering=1
    seats = 4

    def __init__(self, carName, speed):
        self.carName = carName
        self.spee = speed
    def display(self):
       print(self.carName)
       print(self.steering)
       print(self.seats)
       print(self.wheels)
car = Car("BMW",200)
car.display()

print("\n")

car2 = Car("Land Rover",250)
car2.display()