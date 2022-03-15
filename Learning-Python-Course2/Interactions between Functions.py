# This is a built-in function.
example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from random import shuffle
shuffle(example)
print(example)

# Now we are going to create our own function
# Example:
def shuflle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuflle_list(example)
print(result)
mylist = ["", "O", ""]
print(mylist)

def player_guess():

    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, or 2")

    return int(guess)
print(player_guess())

def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

# Initial list
mylist = ["", "O", ""]

# Shuffle list
mixedup_list = shuflle_list(mylist)

# User guess
guess = player_guess()

# Check guess
check_guess(mixedup_list, guess)


