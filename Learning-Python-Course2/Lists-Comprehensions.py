# Comprehensions list is a way to quickly create a list. Using for loop or append.
# Example:
mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
    print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist2 = [x for x in "word"]
print(mylist2)
mylist3 = [num for num in range(0, 11)]
print(mylist3)
mylist4 = [num**2 for num in range(0, 11)]
print(mylist4)

# You can also add IF statements.
# Example:
mylist5 = [num for num in range(0, 11) if num % 2 == 0]
print(mylist5)
celcius = [0, 10, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# You can also do nested loops.
# Example:
my_list = []
for x in [2, 4, 8, 10]:
    for y in [100, 200, 300, 600]:
        my_list.append(x*y)
        print(my_list)
# Other way with list comprehensions.
my_list2 = [x*y for x in [2, 4, 8, 10] for y in [100, 200, 300, 600]]
print(my_list2)
