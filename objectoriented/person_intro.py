from statistics import multimode


class Person:
    version = 2.5

    def __init__(self,name):
        self.name = name

    # Define a __str__ function to define the class' string name
    def __str__(self):
        return "Mammal"
    #standard method
    def whoami(self):
        # Use return with f instead of a static print statement to build and return a string
        return f"My name is {self.name}"

    @classmethod
    def whatami(cls):
        return f"I'm a Person Class, version {cls.version}"

# This is a way to ensure this part is only run if the script is run 'stand alone'
if __name__ == "__main__":
    p = Person(name="Jim")
    print(p)
    print(p.whoami())
    print(Person.whatami())