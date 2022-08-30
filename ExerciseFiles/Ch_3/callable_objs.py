class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"


    # TODO: the __call__ method can be used to call the object like a function


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher and the Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
