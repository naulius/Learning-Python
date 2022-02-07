# Lists in Python has an order sequence.
# Use brackets and commas.
# YOu can index and slice lists.
# LIst can hold integers, strings, floating numbers in the same list.
# Example:
my_list = ["Natalia", 100, 50.85]
print(my_list)

# You can check the length of the list using len.
# Example:
print(len(my_list)) # Result 3 items in the list.

# If you want to index the list:
print(my_list[0]) # Result: Natalia
print(my_list[1:]) # Result: Print from 100 to the end.

# You can concatenate lists,it will concatenate the 2 list in one.
# Example:
my_other_list = ["Elena", "Iza"]
print(my_list+ my_other_list) # Result, it makes one list from the two lists.

# You can change names in the list.
# Example:
my_second_list = ["Vitaliy", "Kathy", "Elena", "Iza"]
my_second_list[0] = "Vitashka" # Use indexing to change the list.
print(my_second_list)

# You can also add new items to the list, using append method, use parenthesis.
# Example:
my_second_list.append("Natalia")
print(my_second_list)

# If you want to remove an item from the list, use pop method, use parenthesis.
# Example:
my_second_list.pop()
print(my_second_list)

# You can remove a specific item from the list, use pop method and indexing,
# you put the index number between parenthesis.
# Example:
my_second_list.pop(1)
print(my_second_list)

# You can also put in order your list, using sort.
# Example:
my_list = ["a", "f", "e", "i"]
num_list = [15, 1, 8, 20]
num_list.sort()
my_list.sort()
print(my_list)
print(num_list)

# You can reverse the items of your list with reverse method.
# Example:
my_list.reverse()
print(my_list)