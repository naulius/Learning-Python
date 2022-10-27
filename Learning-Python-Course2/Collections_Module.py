# Collections Modules are built-in in python.Implements specialized containers data type.
# Conatainers which are dictionary or Tuples.

from collections import Counter
mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(Counter(mylist))
mylist = ["a", "a", 1, 2]
print(Counter(mylist))
sentence = "How many times does each word show up in this sentence"
print(Counter(sentence.split()))

from collections import defaultdict
d = {"a":10}

from collections import namedtuple
Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="Sam")
print(type(sammy))
print(sammy.name)
print(sammy[0])