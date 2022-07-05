# Handle the exception thrown by the code below by using try and except blocks:
for i in ['a','b','c']:
    print(i**2)
    try:
        for i in ["a", "b", "c"]:
            print(i**2)
    except:
       # print("An error occurred")

# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
       x = 5
       y = 0
       try:
           z = x / y
       except ZeroDivisionError:
           print("Can't divide by Zero!")
       finally:
           print('All Done!')

# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    print('Thank you, your number squared is: ', n ** 2)

