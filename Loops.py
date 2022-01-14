# Practicing for-loops

# I want to repeat 20 times one phrase.
print("---------------")
print("\nExample: for-loop\n")
for x in range(20):
    print("Te amo Vitashka")

# I want to give a condition to the code, which is to print from 1 to 10
print("---------------")
print("\nExample: while-loop\n")
x = 0
while x < 10:
    x+=1
    print(x)

# Iterate over a list and print each value
print("----------------")
print("Example: For-Loop iterating a list")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for each_number in x:
    print(each_number)

# Iterate over values of a Dictionary
print("-----------------")
print("Example: For-Loop iterating over values of a dictionary")
Words = {'Coco': 'Loco',
         'Bro': 'Hermano',
         'Sapo': 'Vivo'
         }
for value in Words.values():
    print(value)

# Iterate over keys of a dictionary
print("-----------------")
print("Example: For-Loop iterating over keys of a dictionary")
Daughter_1 = {'Name': 'Elena', 'Age': 6, 'Born': 'Ottawa'
              }
Daughter_2 = {'Name': 'Iza', 'Age': 4, 'Born': 'Ottawa'
              }
Daughter_3 = {'Name': 'Kathy', 'Age': 18, 'Born': 'Texas'
              }
for key in list(Daughter_1.keys()) + list(Daughter_2.keys()) + list(Daughter_3.keys()):
    print(key)
print("------------------")
print("Example_2 For-Loop iterating over key of a dictionary")
Daughters = {
    'Elena': {'Age': 6, 'Born': 'Ottawa'},
    'Iza': {'Age': 4, 'Born': 'Ottawa'},
    'Kathy': {'Age': 18, 'Born': 'Texas'}
}
for key in Daughters:
    print(key)

# Print all key-values pairs of dictionary
print("------------------")
print(Daughters.items())

