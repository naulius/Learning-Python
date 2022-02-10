# Sets are unordered collection of unique elements. It can be only one that represents an object.
# Example:
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2) # It won't add two times the same number. In sets are only one unique element.
print(my_set)

# You can make a set from a list. It only shows unique elements, no repetitions, no particular order.
# Example:
mylist = [1, 1, 1, 3, 4, 4, 5, 5, 5]
myset = set(mylist)
print(myset)

