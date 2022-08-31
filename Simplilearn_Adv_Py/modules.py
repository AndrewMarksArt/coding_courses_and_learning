# A module is a python file that has t=functions or classes(.py files)
# a python program can use one or more modules
# Modules can have one or more functions
# they help organize your code --> break up into smaller chunks

# Modular programming refers to the process of breaking a large task
# into seperate, smaller, more manageable subtasks or modules

# individual modules can then be grouped together like building blocks
# lots of advantages
# simplicity, maintainability, reusability, scoping

# functions, modules, and packages are all constructs in python
# promoting code modularization

# can import with import key word
import os

# to see all functions in a module
print(dir(os))

# get cwd
print(os.getcwd())

# list of files
print(os.listdir())

# import def from other py file
from iterators import print_brake

# use def from iterators
print_brake()

