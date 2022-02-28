# In range operator is very useful in Python.
# Example:
for num in range(10):
    print(num)

# Enumerate index count automatically, the result is in form of Tuples.
# Example:
word = "abcde"
for item in enumerate(word):
    print(item)

# The zip function pairs your lists.
# Example:
mylist1 = ["a", "b", "c", "d"]
mylist2 = [1, 2, 3, 4]
for item in zip(mylist1, mylist2):
    print(item)
x = "mykey" in {"mykey":365}
print(x)
d = {"mykey":365}
d = 365 in d.values()
print(d)

# Min function helps to find the minimum number in a list.
# Example:
mylist3 = [2,400,100]
a = min(mylist3)
print(a)

# Max function helps to find the maximum number in the list.
# Example:
mylist4 = [5, 500, 100]
b = max(mylist4)
print(b)

# The Shuffle function, rearrange the list.
# Example:
from random import shuffle
mylist5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist5)
print(mylist5)

# Random function gives a random number from the list.
# Example:
from random import randint
d = randint(0, 100)
print(d)

# Input function.
# Example:
result = input("What is your name?")
print(result)
print(type(result))








