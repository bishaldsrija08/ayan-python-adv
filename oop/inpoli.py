class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self): #overriding the move method of Vehicle class
        print("The car is moving.")

class Plane(Vehicle):
    def move(self): #overriding the move method of Vehicle class
        print("The plane is flying.")
        
car1 = Car()
print("Polymorphism Example:")
print(car1.move())  # Output: The car is moving.
plane1 = Plane()
print(plane1.move())  # Output: The plane is flying.