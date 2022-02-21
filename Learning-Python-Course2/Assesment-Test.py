# Description of the following Object Types:

# Numbers:They are two types of objects, it can be Integers, these one represent the whole number (100, 50) and
#         floating numbers, these one are decimal numbers (4.5, 10.98).

# Strings: This is an ordered sequence of characters or words that are wrapped in quotes,
#          It could be in single or double quotes. You can index or slice strings.

# Lists: It's an ordered sequence of strings or/and numbers(integers or floating) that are separated between commas.
#        They are written between square brackets. You can index or slice lists.

# Tuples: They are a list of sequence of character or numbers that can not be changed.
#         They are written between parenthesis. You can  index them or slicing, but it can not be changed the order.

# Dictionaries: It's a list which include a key and value. There is no order.
#               They are written between curly brackets.You can index and slice it.


# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
x = ((200/2) - (5**2)) + (25*1 + 0.25)
print(x)


# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5) = 44
r1 = 4 * (6 + 5)
print(r1)
# What is the value of the expression 4 * 6 + 5  = 29
r2 = 4 * 6 + 5
print(r2)
# What is the value of the expression 4 + 6 * 5 = 34
r3 = 4 + 6 * 5
print(r3)


# What is the type of the result of the expression 3 + 1.5 + 4?
r4 = 3 + 1.5 + 4
print(r4)
# The type of this result is a floating number.


# What would you use to find a number’s square root, as well as its square?
# To find the square:
a = 4**2
print(a)
# To find its square root:
b= 4**0.5
print(b)


# Strings
# Given the string 'hello' give an index command that returns 'e'.
s = "Hello"
print(s[1])
# Reverse the string 'hello' using slicing:
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s[4])
# Method 2:
print(s[-1])


# Lists
# Build this list [0,0,0] two separate ways.
# Method 1:
list1 = [0,0,0]
print(list1)
# Method 2:
list2 = [0] * 3
print(list2)
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "Goodbye"
print(list3)
# Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)


# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d["simple_key"])
d2 = {"k1":{"k2":"hello"}}
print(d2["k1"]["k2"])
d3 = {"k1":[{"nest_key":['this is deep',['hello']]}]}
print(d3["k1"][0]["nest_key"][1][0])
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4["k1"][2]["k2"][1]["tough"][2][0])

# Can you sort a dictionary? Why or why not?
# No you can not sort it.They are unordered objects.


# Tuples
# What is the major difference between tuples and lists? How do you create a tuple?
# The difference is that Tuples you can not change it. You can not change position or alter them.
# You create a Tuple with parenthesis.

# Sets
# What is unique about a set? Use a set to find the unique values of the list below:
# Sets are unordered collection of unique elements. One element represents one object.
list5 = [1,2,2,33,4,4,11,22,3,3,2]
myset = set(list5)
print(myset)


# Booleans
# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
x = 2 > 3
print(x)
y = 3 <= 2
print(y)
z = 3 == 2.0
print(z)
a = 3.0 == 3
print(a)
b = 4**0.5 != 2
print(b)

# Final Question: What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1']) # False








