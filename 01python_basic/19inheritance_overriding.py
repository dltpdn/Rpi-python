class A:
    def __init__(self):
        print 'A.__init__()'
    def method(self):
        print 'method A'

class B(A):
    def method(self):
        print 'method B'
        
a = A()
b = B()
a.method()
b.method()

    