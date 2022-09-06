class Borg:
    """The borg design pattern"""

    _shared_data = {} # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # make an attribute dictionary


class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)

# create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")

# print the object
print(x)

# second singleton object
y = Singleton(SNMP = "Simple Network Management Protocol")

# print the object
print(y)
