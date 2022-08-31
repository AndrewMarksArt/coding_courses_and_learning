# Creating Immutable dataclasses

from dataclasses import dataclass


# TODO: the Frozen parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newValue):
        self.value2 = newValue


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "new value"

# TODO: even functions within the class can't change anything
obj.somefunc(10)