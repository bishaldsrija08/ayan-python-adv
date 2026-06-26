class Animal: # parent class
    def speak (self):
        print("Animal speaks")

class Dog(Animal): # child class
    def walk(self):
        print("Dog walks on all fours")

dog = Dog()
print(dog.speak()) # calling parent class method