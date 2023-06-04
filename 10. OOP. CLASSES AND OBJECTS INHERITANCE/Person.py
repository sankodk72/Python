# Create a class Human, everyone has a name, create a method in the 
# class that displays a welcome message to each person. Create a class method 
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
     def __init__(self, name):
        self.name = name
    
     def welcome(self):
        return f"Hello, {self.name}"

     @classmethod
     def classmethod(cls, species = "Homosapiens"):
        cls.species = species
        return cls.species

     @staticmethod
     def staticmethod():
        return 'arbitrary message called'

h1 = Human("John")

print(h1.welcome())
print(Human.welcome(h1))

print(h1.classmethod())
print(Human.classmethod())

print(h1.staticmethod())
print(Human.staticmethod())
