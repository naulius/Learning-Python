# Python has decorators that allow you to tack on extra funcionality to an already
# existing function. They use the @ operator and are then placed on top of the original function.
# Example:
def hello():
    return "Hello!"
#print (hello())

def hello(name = "Natalia"):
    print("The Hello() function has been executed!")

    def greet():
        return "\t This is the greet() func inside Hello!"

    def welcome():
        return "\t THis is welcome() inside Hello"

    print(greet())
    print(welcome())
    print("This is the end of Hello function")

    if name == "Natalia":
        return greet
    else:
        return welcome

print(hello())


def cool():

    def super_cool():
        return "I'm very cool"
    return super_cool

some_func = cool()
print(some_func())


def hello():
    return "Hi Natalia"

def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())

print(hello())


def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before original function")
        original_func()
        print("Some extra code, after the original code")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

print(func_needs_decorator())
decorated_func = new_decorator(func_needs_decorator)
print(decorated_func())

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

print(decorated_func())