# Understanding class inheritance

class Book:
    def __init__(self, title, author, pages, price) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
m1 = Magazine("Scientific American", "Spring Nature", 5.99, "Monthly")
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
