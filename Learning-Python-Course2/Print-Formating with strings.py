# Instead of concatenate using the sign +, we can use the .format method.
# The way to write the .format method. print("String{}".format(new string"))
# Example:
print("This a whole phrase for {}".format("Natalia"))
# you can also concatenate several strings.
# Example:
print("the Fox {} {} {}".format("black", "blue", "green"))
# You can index your strings to have a specific order.
# Example:
print("the fox {2} {1} {0}".format("black", "blue", "green"))

# You can even add variables to the strings.
# Example:
print ("The weather is {a} {b} {c}".format(a= "cold", b= "grey", c="snowy"))

# You can concatenate floating numbers.
# Example:
answer = 200/15
print("This is the answer {}".format(answer))
# You can even give decimal precision. {value:width.precisionf)
# Example:
print("This is the answer {x:1.3f}".format(x= answer))

# Other way to formatting:
# Example:
name= "Vitaliy"
age = 38
print( f'Su nombre es {name}')
# You can have multiple variables.
# Example:
print(f'His name is {name}, He is {age} old')
