class Encapsulation:
    def __init__(self):
        self.public = "public"
        self.__private = "private"
    
    def show(self):
        print self.public, self.__private


obj = Encapsulation()
obj.show()
print obj.public#, obj.__private