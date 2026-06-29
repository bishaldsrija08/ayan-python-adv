# polymorphism -> Many forms [The word "polymorphism" means "many forms"]
x= "Hello"
y = [1, 2, 3]
z = {
    "a": 1,
    "b": 2
}

print(len(x))  # Output: 5
print(len(y))  # Output: 3
print(len(z))  # Output: 2

class Car:
    def move(self):
        print("Car is moving")
        
class Bike:
    def move(self):
        print("Bike is moving")

class Truck:
    def move(self):
        print("Truck is moving")

class Bus:
    def move(self):
        print("Bus is moving")

class Plane:
    def move(self):
        print("Plane is flying")

car1 = Car()
bike1 = Bike()
truck1 = Truck()
plane1 = Plane()
bus1 = Bus()

print("Polymorphism Example:")
print(car1.move())  # Output: Car is moving
print(bike1.move())  # Output: Bike is moving
print(truck1.move())  # Output: Truck is moving
print(plane1.move())  # Output: Plane is flying
print(bus1.move())  # Output: Bus is moving