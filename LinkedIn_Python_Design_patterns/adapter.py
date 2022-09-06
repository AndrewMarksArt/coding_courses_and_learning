class Korean:
    """Korean Speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names"""
    def __init__(self, object, **adapt_method):
        self._object = object

        self.__dict__.update(adapt_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []

korean = Korean()
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
