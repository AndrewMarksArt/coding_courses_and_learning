class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1


    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"


    # TODO: __getattribute__ called when an attr is retieved
    #def __getattribute__(self, name):
    #    if name == "price":
    #        p = super().__getattribute__("price")
    #        d = super().__getattribute__("_discount")
    #        return p - (p * d)
    #    else:
    #        return super().__getattribute__(name)


    # TODO: __setattr__ called when an attribute value is set
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("the price attr must be a float")
        return super().__setattr__(name, value)


    # TODO: __getattr__ called when __getattribute__ lookup fails
    def __getattr__(self, name):
        return name + " is not here"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher and the Rye", "JD Salinger", 29.95)

b1.price = 38.95
print(b1)

b2.price = float(40)
print(b2)

print(b1.randomprop)

