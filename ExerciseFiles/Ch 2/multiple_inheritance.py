

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class a"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class b"


# when inheriting from multiple classes that have methods and properties with the same name
# it will use the ones from the class listed first, in this case Class B
class C(B, A):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.showProps()

# __mro__ is the method resolution order
print(C.__mro__)
