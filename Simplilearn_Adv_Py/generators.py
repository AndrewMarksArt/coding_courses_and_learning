# uses yield instead of return keyword
# key difference between the 'yield' and 'return' is that
# yield returns a calue and pauses the execution while
# maintaining the internal states, wheras the return statement
# returns a value and terminates the execution of the function

# generator = iterator with memory (sort of)

from re import A


def myGenerator():
    print('First')
    yield 10

    print('Second')
    yield 20

    print('Last')
    yield 30

gen = myGenerator()

next(gen)
next(gen)
next(gen)
# stop iteration error
next(gen)

# use generator with a for loop
def getSequenceUpTo(x):
    for i in range(x):
        yield i

seq = getSequenceUpTo(2)
next(seq)

# fib sequence
def fibonacci(max):
    a, b, = 0, 1

    while a < max:
        yield a
        a, b = b, a+b

