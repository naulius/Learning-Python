x =25
def printer():
    x = 50
    return x
print(x)
print(printer())

# LEGB Rule:
# L: Local: Names assigned in any way within a function(def or lambda), and not declared global in that function.
# E: Enclosing function locals: Names in the local scope of any and all enclosing functions(def or lambda) from inner to outer.
# G: Global (module): Names assigned at the top level of a module file or declared global in a def within a file.
# B: Built-in Python: Names preassigned in the built-in names module: open, range, SyntaxError..

# Example of Local: lambda num: num ** 2
# Example of Enclosing function:

# Global
name = "This is a global string"

def greet():
    # Enclosing
    name = "Sammy"

    def hello():
        # Local
        print("Hello " + name)

    hello()
print(greet())

x = 50
def func(x):
    print(f"x is {x}")
    x = 200
    print(f"I just locally changed x to {x}")
print(func(x))
