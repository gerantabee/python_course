# Let's define a Mammal class to serve as a blue print for other mammals
# class Mammal()...

class Mammal:
    # Variable stub
    # Use underscore for 'private' naming convention
    _cals: int

    def __init__(self, cals):
        # We will deprecrate the need for type with subclassing
        self._cals = cals

    def __str__(self):
        return "Mammal Class"


# Pass lets us define a stem for a method without an implementatio
# we cna override these later


# Person class subclasses Mammal
class Person(Mammal):

    # These first two methods are overrides
    def __init__(self, cals, name):
        # self.energy(cals)
        self._cals = cals

    def __str__(self):
        return "Person class"




# Use this condition to ensure this code only runs when the script is called directly
if __name__ == "__main__":
   print("this will run if we are executing this script directly")
