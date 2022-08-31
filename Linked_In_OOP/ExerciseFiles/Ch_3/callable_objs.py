class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"


    # TODO: the __call__ method can be used to call the object like a function
    # good for object that change frequently or have attributes that change together,
    # more compact and easy to read
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher and the Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
print(b1)
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
