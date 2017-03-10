import sys

a = 10
print a
print type(a)
x = a
print id(a), id(x)
print a is x
del x
#print x  #error 
print a.bit_length()

b = 20
print a + b

c = 'hello'
print c


