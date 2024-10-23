from abc import ABC, abstractmethod

class Mammal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Mammal):
    _type:str
    _instances = []
    def __init__(self,type):
        self._type = type
        # Singleton implemenation
        # if self.totalDogs() > 0:
        #     print("you already have a dog")
        #     # Don't use quit, or you'll end the program
        #     return
        # else:
        #     Dog._instances.append(self)
        Dog._instances.append(self)

    def eat(self):
        print("This {} is eating".format(self._type))

    def sleep(self):
        print("Zzzzzzz")

    # Class methods operate at the class (vs. instance) level and are useful for a variety of situations
    @classmethod
    def totalDogs(cls):
        return len(cls._instances)


fido =  Dog("Yorkie")
fido.eat()
fido.sleep()
print(Dog.totalDogs())
rey = Dog("Morkie")
print(Dog.totalDogs())
fido.sleep()