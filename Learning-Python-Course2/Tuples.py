# Tuples are similar to lists but tuples you can not change it.
# Once an element is inside a tuple it can to be altered, reassigned. You find an index position you can not change it.
# In Tuples we use parenthesis.
# Example:
t = (1, 2, 3)
my_list = [12, 22, 34]
print(t) # T runs tuples.
print(my_list)
print(len(t)) # Runs 3, because there are 3 elements.
t = ("one", 100)
print(t[0])
print(t[-1])

# You can also find how many elements of the same character there are, use count.
# Example:
t = ("e", "e", "e","i", "o")
print(t.count("e")) # It counts 3 times "e".
# You can also find the index of those multiple elements, it returns the first index of the first element.
# Example:
print(t.index("e"))

# The elements in a Tuples can't be changed.
# Example:
t2 = ("camara", "food", "clothing", "tent")
t2[2] = "Warm clothing"
print(t2)
#
list2 = ["camara", "food", "clothing", "tent"]
list2[2] = "Warm clothing"
print(list2) # In this case, because is a list, it replaced clothing for warm clothing.

