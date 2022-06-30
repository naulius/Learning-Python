# We can use error and handling to attempt to plan for possible errors.
# When you use error handling the code can still be running.
# We use 3 keywords:
# try: This is the block of code to be attempted (may lead to an error)
# except: Block of code will execute in case there is an error in try block.
# finally: A final code of block to be executed, regardless of an error.
# Example:
def add(n1, n2):
    print(n1 + n2)
add(20, 30)
number1 = 10
#number2 = input("PLease provide a number: ")
#add(number1, number2)
#print(add)

#try:
    #result = 10 + "10"
#except:
   #print("It looks like you are not adding correctly")
#else:
   #print("went well")
   #print(result)

try:
    f = open("testfile", "r")
    f.write("write test line")
except TypeError:
    print("there was a type of error")
except OSError:
    print("Hey you have an OSError")
finally:
    print("I always run")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide numer: "))
        except:
            print("Whoops! that is not a number")
            continue
        else:
            print("THank you")
            break

        finally:
            print("End of try/except/final")
            print("It always run at the end!")
print(ask_for_int())







