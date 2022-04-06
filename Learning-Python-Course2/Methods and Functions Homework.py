# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as : (4/3)πr3

def vol(rad):
    return (4/3) * (3.14) * (rad ** 3)
print(vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if num in range(low, high + 1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')
print(ran_check(5, 2, 7))

def ran_bool(num,low,high):
    return num in range(low,high+1)
print(ran_bool(3,1,10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

s = "Hello Mr. Rogers, how are you this fine Tuesday?"

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply([1,2,3,-4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]
print(palindrome('nurses run'))
print(palindrome('abcba'))


