# use Class level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create class method

    # TODO: create a static method

    # instance methods recieve a specific object instance as an argument
    # and operate on data specific to that object
    def setTitle(self, new_title):
        self.title = new_title

    def __init__(self, title):
        self.title = title


# TODO: access the class attribute

# TODO: create some book instances
b1 = Book("Title 1")
b2 = Book("Title 2")
