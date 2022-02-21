# Table of Comparison Operators:
# In the table below, a=3 and b=4.
# == 	(a == b) is not true.
# != 	(a != b) is true
# > 	(a > b) is not true.
# < 	(a < b) is true.
# >= 	(a >= b) is not true.
# <= 	(a <= b) is true.

# Example:
print(2 == 2)
print(2 == 1)
print("Bye" == "bye")
print(3 != 3)
print(4 != 4)
print(2 > 3)
print(5 > 4)
print(1 < 2)
print( 2 >= 2)
print(1 <= 2)

# Chaining Comparison Operators.
# We can use logical operators to combine comparisons: AND, OR, NOT.
# Examples:
print(1 < 2 < 3)
x = 1 < 2 and 2 < 3
print(x)
print("h" == "h" and 1 <= 4)
print(100 == 1 or 2 < 6)  # Only needs one to be true and the result will be TRUE.
print(not 1 == 1)  # It returns the opposite statement.
print(not 400 > 5000)

