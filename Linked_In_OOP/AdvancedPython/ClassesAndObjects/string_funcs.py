"""
Class String Functions and examples
 - object.__str__ --> str(object), print(object), "{0}".format(object)
 - __repr__ --> should return a description that lets you recreate the object
 - __format__ --> format_spec to how to format
 - __Bytes__
"""


class Person():
    def __init__(self) -> None:
        self.fname = "Andrew"
        self.lname = "Marks"
        self.age = 36

    def __repr__(self) -> str:
        return "<Person Class - fname:{0}, lname:{1}, age:{2}>".format(
            self.fname, self.lname, self.age
        )

    def __str__(self) -> str:
        return "Person ({0} {1} is {2} years old)".format(
            self.fname, self.lname, self.age
        )

    def __bytes__(self):
        val = "Person ({0} {1} is {2} years old)".format(
            self.fname, self.lname, self.age
        )
        return bytes(val.encode('utf-8'))


def main():
    # create new person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formated: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
