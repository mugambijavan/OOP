class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} makes a generic movement.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running. 🐾")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying. ✈️")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming. 🐠")

def animal_actions(animals):
    """
    Takes a list of Animal objects and calls their move() method.
    """
    for animal in animals:
        animal.move()

# Creating instances of different animal classes
dog1 = Dog("Buddy")
bird1 = Bird("Tweety")
fish1 = Fish("Nemo")

animals_list = [dog1, bird1, fish1]

# Demonstrating polymorphism
animal_actions(animals_list)