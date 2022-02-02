# For indexing a string you count from 0.Use square brackets.
# Example:
myname= "Natalia"
print(myname[0])
# You can also use negative index, but this starts from the end.
# Example:
myname = "Natalia"
print(myname[-4])

# For slicing use index. You index some parts of the string.
# For Example:
mypet = "mouse"
print(mypet[1:])
print(mypet[:-1])
print(mypet[1:3]) # In this number 1 is where the slice starts and 3 where it end and it does not include
                  # the character of that number, it means it does not include letter s. When you run it
                  # the answer is OU.
# You can use double : : when you run, the result is the complete word form the start to the end.
# Example:
myname = "Natalia"
print(myname[::])
# But if you want to jump each index number you specify that.
# Example:
print(myname[::2]) # It starts with the first letter N and then jump every 2 letters. Result Ntla.
print(myname[2::2]) # It starts from the position two without counting it. Result tla.
# To reverse a string use double ::-1.
# Example:
myname = "Natalia"
print(myname[::-1])
