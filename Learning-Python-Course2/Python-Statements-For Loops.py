# We can use For loops to execute a block of code for every iteration in a string.
# Iterate means you can perform am action for every character in a string.
# A string is an iterable object, you can work through it.
# A list is iterable, you can go through a list.
# Syntax of a For a loop:
# Example:
mylist = [1, 2, 3, 4, 5]
for num in mylist:
    print(num)
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number:{num}")

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

my_string = "Hello World"
for phrase in my_string:
    print(phrase)

# If you want you can't assign a variable and use underscore.
# Example:
for _ in "Hello World":
    print("Hi")

# You can use this iteration for Tuples:
# Example:
tup = (1, 2, 3)
for num in tup:
    print(num)
my_list2 = [(1, 2), (2, 3), (4,5)]
for pairs in my_list2:
    print(pairs)

# You can also do Tuple packing.
for a,b in my_list2:
    print(a)

my_list3 =[(1, 2, 3), (4, 5, 6),(7, 8, 9)]
for a, b, c in my_list3:
    print(b)

# You can also iterate through a dictionary.
# Example:
d = {"k1": 1, "k2": 2, "k3": 3}
for pairs3 in d:
    print(pairs3)    # By default print the key of the dictionary.
# If I want the key and value:
for key,value in d.items():
    print(key,value)
for value in d.values():
    print(value)







