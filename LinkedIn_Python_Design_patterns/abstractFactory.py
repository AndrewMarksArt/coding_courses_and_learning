class Dog:
    """
    One of the objects to be returned
    """

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """
    Concrete Factory
    """

    def get_pet(self):
        """
        Returns a Dog object
        """
        return Dog()

    def get_food(self):
        """
        return a Dog Food object
        """
        return "Dog Food!"


class PetStore:
    """
    Pet store houses our Abstract Factory
    """

    def __init__(self, pet_factory=None):
        """
        pet_factory is our abstract factory
        """
        self._pet_factory = pet_factory

    def show_pet(self):
        """
        Utility method to display the details of the objects returned
        """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is a '{}'!".format(pet))
        print("Our pet says hello by saying '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))


# create concrete factrory
factory = DogFactory()

# create pet store
shop = PetStore(factory)

# invoke utility method
shop.show_pet()
