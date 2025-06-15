class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return "Woof"
    


# dog1 = Dog("Buddy", "Pitbull")
# dog2 = Dog("Sivi", "Brakan")

# print(f"{dog1.name} is a {dog1.breed} he says {dog1.bark()}")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Lion(Animal):
    def speak(self):
        return f"The {self.name} roars"