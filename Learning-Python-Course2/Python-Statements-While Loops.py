# While Loops continue to execute a code while some condition remains true.
# Syntax for While Loops:
# While some_boolean_condition:
     # Do something (Block of code)
# You can add else condition:
# else:
     # Do something different
# Example:
x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1
# Useful keywords to use with While Loops: BREAK, CONTINUE,PASS.
# Break: Break the current Loop.
# Continue: Goes to the top Loop.
# Pass: Does nothing.
# Example:
x = [1, 2, 3, 4]
for item in x:
    pass
print("The end")
my_string = "Natalia"
for letter in my_string:
    if letter == "a":
        continue
    print(letter)
my_string2 = "Vitaliy"
for letter in my_string2:
    if letter == "a":
        break
    print(letter)
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1


