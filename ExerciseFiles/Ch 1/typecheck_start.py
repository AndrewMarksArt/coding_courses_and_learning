# Checking class types and instances

from unicodedata import name


class Book:
    def __init__(self, title) -> None:
        self.title = title


class Newspaper:
    def __init__(self, name) -> None:
        self.name = name


# create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")
