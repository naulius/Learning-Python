# Strings are immutable, you can't change them.
# Example:
name = "Sam"
# name[0]="p" # It doesn't work
# If you want to change the string you need to concatenate, for this you use the plus sign +.
# Example:
last_letters = name[1:]
print(last_letters)
x = "P" + last_letters
print(x) # Result is Pam

# You can also multiple your string.
# Example:
x = "N"
print(x * 10)

# You have to be careful with string concatenation. If you want to do a mathematical operation, for example
# addition, you don't use quotes for that, but if you want to concatenate number you use quotes.
# Example:
x = 2 + 3
print(x) # Result 5.
x = "2" + "3"
print(x)  # Result 23.

# If you want to change lower letters to upper letters. Use the word upper.
# Example:
x = "maria"
print(x.upper()) # Result, it changes to MARIA
# The same if you want to change upper letters to lower letters. Write lower and pass the method.
# Example:
x ="ELENA"
print(x.lower()) # It changes to lower letters, elena.

# You can also split the string. Using the word split.
# Example:
x = "Hola World"
print(x.split()) # Divide the two words. ["Hola, "World"], it's between brackets because it became a list.

# You can remove letters of the string using splitting.
# Example:
x = "Hola to everyone in this world". # It doesn't show the letter "i" in the whole phrase.
print(x.split("i"))


