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
