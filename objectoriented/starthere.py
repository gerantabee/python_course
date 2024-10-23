'''
Classes define a blue print for resuable objects in your code. Each class (object) has attributes
(values that describe the class or are unique to each instance/copy) methods (functions that perform some type
of external or internal task). Classes are building blocks for native Python functionality and libraries
that you may use.

Classes can extend (subclass) others to inherit functionality while adding unique capabilities.

syntax:
class ClassName(ExtendedClass):
    somevar:int
    def __init__(self,value):
        starting code here
        _self.somevar = value

    def someMethod(self,params):
        do something here

cn = new ClassName(20)
cn.someMethod(info)

'''
class Human():
    _name: str
    _age: int

    def __init__(self, name,age):
        self._name = name
        self._age = age
        # print("I'm a new human named {}.".format(name))

    def __str__(self):
        return "Human"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class Runner(Human):
    def __init__(self, name,age):
        super().__init__(name,age)
        self._name = name
        print("I'm a new runner named {}.".format(name))

    def __str__(self):
        return "Runner"

    def run(self):
        print("Running...")


class Chef(Human):
    def __init__(self, name,age):
        self._name = name
        super().__init__(name,age)
        print("I'm a new chef named {}.".format(name))

    def __str__(self):
        return "Chef"

    def cook(self):
        print("Cooking...")


# You could simply pass occupation as an attribute, but if that occupation has
# a good deal of distinct functionality this isn't practical
gordon = Chef("Gordon",57)
sam = Runner("Sam",35)


print(gordon.age)
gordon.specialty = "Something else"
print(gordon.specialty)