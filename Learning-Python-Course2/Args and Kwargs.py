def myfunc(a, b):
    # Returns 5% of the sum a and b
    return sum((a, b)) * 0.05
result = myfunc(40, 60)
print(result)

# When I want to have may positional arguments in my function I use *args.This args returns Tuples.
# Example:
def myfunc(*args):
    return sum(args) * 0.05
result = myfunc(40, 60, 100, 1, 34)
print(result)

# I use **Kwargs returns a dictionary.
# Example:
def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")

result = myfunc(fruit = "apple", veggie = "lettuce")

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}". format(args[0], kwargs["food"]))

result = myfunc (10, 20, 50, fuit = "apple",food = "eggs" )



