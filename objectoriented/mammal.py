from typing import Final,final

class Mammal:
    # Variable stub
    # Use underscore for 'private' naming convention
    _cals: int

    def __init__(self, cals):
        # We will deprecrate the need for type with subclassing
        self._cals = cals

    def __str__(self):
        return "Mammal Class"

    def eat(self, cals):
        # self.cals = cals
        self._cals += cals
        print("Eating {} calories".format(cals))
    # add @final to highlight issues
    def sleep(self):
        print("Zzzzzz")

    def move(self):
        print("Moving")
        # Make sure we're not forcing a move if we have no energy
        if (self.energy != 0):
            self._cals -= 10
        else:
            print("You don't have enough energy to move. Try eating!")

    @property
    def energy(self):
        return self._cals

    @energy.setter
    def energy(self, cals):
        self._cals += cals

    # Pass lets us define a stem for a method without an implementatio
    # we cna override these later


# Person class subclasses Mammal
class Person(Mammal):
    _name: str
    # These first two methods are overrides
    def __init__(self, cals, name):
        # self.energy(cals)
        self._cals = cals
        self.myname = name
        print("Hey guys, my name is {}".format(name))
        # User super() to pass params up to the master class
        super().__init__(cals)

    def __str__(self):
        return "Person class"

    def sleep(self):
        print("This is how people sleep")

    # Getter and setter
    @property
    def myname(self):
        return self._name

    @myname.setter
    def myname(self, name):
        if (name != ""):
            self._name = name

    # Unique method for this subclass
    def speak(self, text):
        print(text)


# Use this condition to ensure this code only runs when the script is called directly
if __name__ == "__main__":
    p = Person(100, "Ingrid")
    print(p.energy)
    p.sleep()
    p.move()
    p.move()
    print(p.energy)
    # This should augment our energy by 50
    # Let's debug this line
    p.eat(50)
    print(p.energy)
    p.speak("Hello there.")
    # This will also work below with a regular assignment '='
    p.energy += 100
    print(p.energy)
    print(p.myname)
    p.myname = "Fred"
    print(p.myname)
