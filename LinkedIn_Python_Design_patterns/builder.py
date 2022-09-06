"""
anti pattern to telescoping, solve to many consturctors/simplify complex objects
partitioned into 4 parts/roles

builder pattern:
1. director - oversees the object being built
2. abstract builder - all needed interfaces to build
3. concrete builder - implements the interfaces
4. product - object being built 
"""

# build a car object and print it 

from distutils.command.build import build


class Director():
    """director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """abstract builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """concrete builder --> provides parts and tools to work on"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "regular tires"

    def add_engine(self):
        self.car.engine = "Turbo"


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)
