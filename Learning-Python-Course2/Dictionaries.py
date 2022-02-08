# Dictionaries stores unordered objects.
# Dictionaries has a key and value.
# Helps to grab objects without knowing the index location.
# Dictionaries uses curly brackets, use colons when write key and value.
# Example:
# {"key1": "value1", "key2": "value2"}
# For dictionaries you grab a value, passing a key.
# Example:
my_dict = {"key1":"value1"} # To assign key and values use curly brackets.
print(my_dict["key1"]) # when you call it use brackets.
my_products = {"pineapple": 4.00, "grapes":5.99}
print(my_products["grapes"])

# You can make lists and dictionaries inside the dictionary.
# Example:
my_dict2 = {"apples":4.95, "t-shirts":["M","L"], "Vegetables":{"carrots":2.50, "leek":5.45}}
print(my_dict2["t-shirts"])
print(my_dict2["Vegetables"]["carrots"])

# You can change the values of your keys, that means make then upper letter or low,etc.
# Example:
my_dict5 = {"value5":["beans", "peaches", 100]}
print(my_dict5["value5"][1].upper())

# You can also add key and values to the dictionary.
# Example:
my_dict6 = {"key1":100, "key2":200}
my_dict6 ["key3"]= 300
print(my_dict6)

# You can also add a new value to the key.
# Example:
my_dict6 = {"key1":100, "key2":200}
my_dict6 ["key1"]= 105
print(my_dict6)

#If you want to know all the keys, values and pairs of the dictionary:
d = {"one": "Hello", "two": "Bye", "three": "Wait"}
print(d.keys())
print(d.values())
print(d.items()) # Use the word item to know the pairs.



