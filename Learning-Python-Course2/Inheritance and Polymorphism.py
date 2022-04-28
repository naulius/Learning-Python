# Inheritance is a way to create classes from existing classes.

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_I(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

my_animal = Animal()
print(my_animal.eat())
print(my_animal.who_am_I())

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_I(self):
        print("I am a dog")

    def bark(self):
        print("!WOOF!")

mydog = Dog()
mydog.who_am_I()
mydog.bark()

# Pholymorphism

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))

