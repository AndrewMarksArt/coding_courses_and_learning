# starting with python 3.7 -- dataclasses decorator for classes that mostly just hold data
# Using data classes to represent data objects
from dataclasses import dataclass
from turtle import title

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author} and its {self.pages} pages long"


    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher and the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
#print(b1.title)
#print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
#print(b1)

# TODO: comparing two dataclasses - they implement __eq__
#print(b1 == b3)

# TODO: change some attributes
#b1.title = "Anna Karenina"
#b1.pages = 864
#print(b1.bookinfo())

# TODO: use the description attribute
print(b1.description)
print(b2.description)
