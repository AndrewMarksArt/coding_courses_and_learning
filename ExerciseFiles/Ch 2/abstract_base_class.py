# Using Abstract Base Classes to enforce class constraints

class GraphicShape:
    def __init__(self) -> None:
        super().__init__()

    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius) -> None:
        self.radius = radius

    
class Square(GraphicShape):
    def __init__(self, side) -> None:
        self.side = side


g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
