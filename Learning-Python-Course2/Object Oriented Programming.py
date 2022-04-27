# OOP allows to create the user their own methods.
# OOP allows us to create code that is repeatable and organized.

class NameOfClass():

    def __init__(self, parm1, parm2):
        self.parm1 = parm1
        self.parm2 = parm2

    def some_method(self):
        print(self.parm1)

# Attributes and Class keyword

mylist = [1, 2, 3]
myset = set()
print(type(myset))
print(type(mylist))

class Sample():
    pass
my_sample = Sample()
print(type(my_sample))

class Dog():    # Name capitalized
    def __init__(self, breed, name, spots):    # "init" is a method, "self" is the instance of the object itself.
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog(breed = "Lab", name = "Sammy", spots = False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.bark(10))

# Class Object Attributes
# Methods are functions that we find inside the body of the class.
# Attributes never has parenthesis.
# Methods need parenthesis to be called.

class Circle():
    # Class object attribute
    pi = 3.14
    def __init__(self, radius=1):    # Init is a special method, we pass  an argument that defines a circle.
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())





