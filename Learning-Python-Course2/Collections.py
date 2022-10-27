from collections import Counter
mylist = [1, 1, 2, 2, 2, 3, 3, 4]
print(Counter(mylist))

mylist2 = ["a", "b", "c", 5, 6, 8]
print(Counter(mylist2))

sentence = "How many times does each word show up in this sentence"
print(Counter(sentence.split()))
print(Counter(c.most_common))