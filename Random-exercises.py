x = 5
if x % 2 == 0:
    print("Perfect")
else:
    print("que mal")

# Concatenate strings
# Example:
name = "Vitaliy"
greet = "Hola"
greeting = greet + " "  + name
print(greeting)
# To concatenate strings use addition symbol + without single or double quote. For spaces use  double quotes between spaces.
# You can also add numbers.
print(3 * "nat")

# While loops and for loops.
# Example, While loops:
n = 0
while(n < 5):
    #print(n)
     n = n + 1

# For loops.
# Example:
for n in range (5):
    print(n)

my_sum = 0
for i in range (7,10):
    my_sum += i
print(my_sum)

# To use break.
# Example:
my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        print(my_sum)




