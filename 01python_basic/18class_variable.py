class MyClass:
    variable1 = 10
    variable2 = 20
    def __init__(self):
        self.variable1 = 100
        self.variable3 = 200

my = MyClass()
print MyClass.variable1, my.variable1
print MyClass.variable2, my.variable2
#print MyClass.variable3
print my.variable3


my2 = MyClass()
MyClass.variable1 = 20
my2.variable1 = 200
print MyClass.variable1, my.variable1, my2.variable1

MyClass.variable9 = 90
my.variable9 = 900
print MyClass.variable9, my.variable9, my2.variable9