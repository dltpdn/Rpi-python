from abc import abstractmethod, ABCMeta
class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        pass
    
class Concrete(Abstract):
    def method(self):
        print('This is concrete class')

#abs = Abstract() #error
con = Concrete()
con.method()