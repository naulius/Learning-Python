from testflows.core import *

with Example("If, else, conditions, concatenate strings, while loops, for loops"):

    with Example("If, else, conditions"):
        x = 5
        if x % 2 == 0:
            note("Perfect")
        else:
            note("que mal")

    with Example("Concatenate strings"):
        name = "Vitaliy"
        greet = "Hola"
        greeting = greet + " "  + name
        note(greeting)
        note(3 * "nat")

    with Example("While loops"):
        n = 0
        while(n < 5):
             note(n)
             n = n + 1

    with Example("for loops"):
        for n in range (5):
            note(n)

        my_sum = 0
        for i in range (7,10):
            my_sum += i
        note(my_sum)

    with Example("for loops using break"):
        my_sum = 0
        for i in range(5, 11, 2):
            my_sum += i
            if my_sum == 5:
                break
                note(my_sum)




