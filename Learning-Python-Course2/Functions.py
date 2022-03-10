# Functions are blocks of code that can be repeated many times.You don't need to write it over and over.
# def Keyword allows you to create functions, def keywords tells Python that this is a function.
# Use snake casing to build a function, they are in lowercase and separate the words with underscore.
# Parenthesis at the end, then you can pass arguments.After this use colons, this indicates an upcoming
# indented code, everything indented is part of the function.
# Example:
def name_of_function(name):
    '''Something you want to comment.
    '''
    name_of_function("Nat")
    print("hello" + name)

def say_hello(name):
    print(f'hello {name}')

say_hello("Nat")

def add_num(num1, num2):
    return num1 + num2

print(add_num(10, 28) + 2)

def even_check(number):
    return number % 2 == 0

print(even_check(20))

# Return True if any number is even inside a list.
def check_even_number(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_number([2, 6, 8]))
print(check_even_number([1, 5, 7]))

# To return all the even numbers in the last example.
def check_even_list(num_list):

    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

print(check_even_list([2, 6, 8, 10, 25]))





