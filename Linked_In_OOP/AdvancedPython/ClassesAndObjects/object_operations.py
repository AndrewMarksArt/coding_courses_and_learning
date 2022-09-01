"""
Class Numerical Operators --> some examples

__iadd__ --> self += other
__isub__ --> self -= other
__imul__ --> self *= other
__itruediv__ --> self /= other
__ifloordiv__ --> self //= other
__ipow__ --> self **= other
__iadd__ --> self &= other
__ior__ --> self |= other

Class Comparison Operators --> some examples
__gt__ --> self > other
__ge__ --> self >= other
__eq__ --> self == other

"""


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "<Point x:{0}, y:{1}>".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.yrsService = yrsService

    def __ge__(self, other):
        return self.level >= other.level

    def __gt__(self, other):
        return self.level > other.level

    def __lt__(self, other):
        return self.level < other.level

    def __le__(self, other):
        return self.level <= other.level


def main():
    # declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # add 2 points
    p3 = p1 + p2
    print(p3)

    # subtract 2 points
    p4 = p2 - p1
    print(p4)

    # perform in-place addition
    p1 += p2
    print(p1)

    print()
    print("look at employee class")
    dept = []
    dept.append(Employee("andrew", "marks", 5, 7))
    dept.append(Employee("colleen", "marks", 3, 9))
    dept.append(Employee("siobhan", "marks", 1, 1))
    dept.append(Employee("kaylee", "marks", 2, 6))

    # who is more senior
    print(dept[0] > dept[2])
    print(dept[1] < dept[-1])


if __name__ == "__main__":
    main()
