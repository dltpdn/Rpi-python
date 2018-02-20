class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayHello(self):
        print('Hello! I am %s, %d years old' % (self.name, self.age))
        
    def set_age(self, age):
        self.age = age
        
lee = Person('Lee', 27)
kim = Person('Kim', 23)
lee.sayHello()
kim.sayHello()
lee.set_age(30)
print(lee.name, lee.age)
print(type(lee), lee.__class__.__name__)
print(isinstance(lee, Person))
