import math
#print(help(math))
value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(math.e)
print(math.log(math.e))
print(math.radians(180))

import random
print(random.randint(0, 100))
print(random.seed(42))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

mylist = list(range(0, 20))
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,15, 16, 17, 18 ,19]
print(random.choices(population=mylist, k=10))
