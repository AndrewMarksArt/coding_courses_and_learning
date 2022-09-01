# look at how we can see documentaion and why its good to write it
import collections


def myFunction(arg1, arg2=None):
    # triple quotes for doc strings
    """
    myFunction(arg1, arg2=None) --> just prints out the args

    Parameters:
    arg1: first argument. What ever you feel like passing
    arg2: the second argument, default to None
    """
    print(arg1, arg2)


def main():
    # using map and collections print out __doc__
    print(map.__doc__)
    print(collections.__doc__)

    # use myFunction to print out arguments
    print(myFunction("hello"))
    # use __doc__ to print out doc string of myFunction
    print(myFunction.__doc__)


"""
Some Best Practices:
 - always use triple quotes even if just one line
 - first line should be a summary sentence of functionality
 - Modules: list important classses, functions, exceptions
 - Classes: list important methods
 - Functions: list and explain each parameter one per line
              if there is a return then list it, otherwise omit
              if it raised exceptions list those

NOTE check out PEP 257 for more on docstrings
"""


if __name__ == "__main__":
    main()
