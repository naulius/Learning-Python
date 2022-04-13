# Displaying Information:
#def display(row1, row2, row3):
   #print(row1)
   #print(row2)
   #print(row3)
   #return [row1,row2,row3]

#example_row = [1, 2, 3]
#print(display(example_row, example_row, example_row))

#row1 = ["", "", ""]
#row2 = ["", "", ""]
#row3 = ["", "", ""]
#display(row1, row2, row3)
#row2[1] = "x"
#print(display(row1, row2, row3))

# Accepting User Input
#input("Please enter a value:")
#result = input("Please enter a value:")

# Validating User Input
#def user_choice():
   #choice = input("Please enter a number (0-10)")
   #return int(choice)
#print(user_choice())

#some_value = "100"
#some_value.isdigit()
#print(int(some_value))

#def user_choice():
   #choice = "Wrong"
   #while choice.isdigit() == False:
      #choice = input("Please enter a number (0-10)")
      #if choice.isdigit() == False:
          #print("Sorry that is not a digit")
   #return int(choice)
#print(user_choice())

#def user_choice():

   # Variables

   # Initial
   #choice = "WRONG"
   #acceptable_range = range(0, 10)
   #within_range = False

   # Two conditions to check
   # Digit or within range==False
   #while choice.isdigit() == False or within_range == False:

      #choice = input("Please enter a number (0-10):")

      # Digit check
      #if choice.isdigit() == False:
         #print("Sorry that's not a digit!")

      # Range check
      #if choice.isdigit() == True:
         #if int(choice) in acceptable_range:
            #within_range = True
         #else:
            #print("Sorry, you are out of acceptable range (0-10")
            #within_range = False

   #return int(choice)
#print(user_choice())

game_list = [0, 1, 2]
def display_game(game_list):
   print("Here is the current list")
   print(game_list)
display_game(game_list)

def position_choice():

   # This original choice value can be anything that isn't an integer.
   choice = "wrong"

   # While the choice is not a digit, keep asking for input.
   while choice not in ["0", "1", "2"]:
      # We shouldn't convert here,otherwise we get an error on a wrong input.
      choice = input("Pick a position to replace (0, 1, 2): ")
      if choice not in ["0", "1", "2"]:
         print("Sorry, but you did not choose a valid position(0, 1, 2)")

   return int(choice)
print(position_choice())

def replacement_choice(game_list, position):
   user_placement = input(" Type a string to place at the position: ")
   game_list[position] = user_placement

   return game_list
print(replacement_choice(game_list, 1))

def gameon_choice():
   choice = "wrong"
   while choice not in ["Y", "N"]:
      choice = input("Would you like to keep playing? (Y or N) ")
      if choice not in ["Y", "N"]:
         print("Sorry I didn't understand.Please make sure to choose Y or N")

   if choice == "Y":
      return True
   else:
      return False
print(gameon_choice())

game_on = True
game_list = [0, 1, 2]

while game_on:

   display_game(game_list)
   position = position_choice()
   game_list = replacement_choice(game_list, position)
   display_game(game_list)
   game_on = gameon_choice()
