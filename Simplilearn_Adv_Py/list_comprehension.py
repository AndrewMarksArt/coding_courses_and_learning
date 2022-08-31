# list comprehension offers a shorter syntax when you want
# to create a new list based on the values of an existing list

fruit = ["apple", "orange", "mango", "banana", "cherry"]
newlist = []

for x in fruit:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with comprehension
newlist2 = [each_fruit for each_fruit in fruit if "a" in each_fruit]
print(newlist2)

letters = [x for x in "human"]
print(letters)

# create new lists using for loop and if's on one line, much cleaner way
obj = [("even", i) if i%2==0 else ("odd", i) for i in range(20)]
print(obj)

# can use with functions
def double(x):
    return x**2

dbl = [double(x) for x in range(10)]
print(dbl)

# can also do set and dict comprehensions
text = "life, uh, finds a way, in a great way indeed"

unique_vowels = {each_letter for each_letter in text if each_letter in "aeiou"}
print(unique_vowels)

# dict comprehensions are similare but require additional defining of a key:
squares = {i: i * i for i in range(10)}
print(squares)
