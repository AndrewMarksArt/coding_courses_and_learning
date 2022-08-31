# Using Abstract Base Classes to implement interfaces
from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def toJSON(slef):
        pass


class GraphicShape(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius) -> None:
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"circle\" : {str(self.calcArea())}}}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
