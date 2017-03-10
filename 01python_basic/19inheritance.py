class Base:

    def __init__(self):
        self.name = "base"

    def show(self):
        print self.name

class Derived(Base):
    def __init__(self):
        Base.__init__(self)

base = Base()
base.show()
derived = Derived()
derived.show()

class Base2(object):
    def __init__(self):
        self.name = "Base2"

    def show(self):
        print self.name

class Derived2(Base2):
    def __init__(self):
        super(Derived2, self).__init__()

base2 = Base2()
base2.show()
derived2 = Derived2()
derived2.show()
