from abc import abstractmethod, ABCMeta
class Abstract:
    __metaclass__ = ABCMeta
    @abstractmethod
    def method(self):
        pass
    
class Concrete(Abstract):
    def method(self):
        print 'This is concrete class'

#abs = Abstract() #error
con = Concrete()
con.method()