# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "this is a secret"

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


# TODO: create an instances of the class
b1 = Book("Treasure Island", "Robert Louis Stevenson", 292, 19.95)
b2 = Book("War and Peace", "Leo Tolstoy", 1225, 29.95)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())
