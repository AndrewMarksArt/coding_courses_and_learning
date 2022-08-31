def print_brake():
    print()
    print("---------"*10)
    print()

# Python Iterators
# an iterator si an object that contains a countable number of values
# can be iterated upon, meaning you can traverse through all the values
# object implements the iterator protocol which consists
# of the methods iter() and next()

#simple iterator -- list
for i in [1, 2, 3, 4]:
    print(i)

for char in "python":
    print(char)

for k in {"x": 1, "y": 2}:
    print(k)

print_brake()

# Iterating through an iterator
# the iter() function returns an iterator from them
# we use next() to manually iterate through all the items of an iterator
# when we reach the end and there is no more data to be returned
# it will raise the StopIteration Exception

#simple list
my_list = [1, 4, 7, 0, 8]
# get an iterator using iter()
my_iter = iter(my_list)
# print some
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print_brake()

# comparison between generator and iterator
# generator = we use a function
# iterator = we use iter() and next()

# generator = saves the states fo the local variables every time "yield" pauses the loop
# iterator = doesn't make use of local variables

# generator = not memory efficent
# iterator = more memory efficent