f = lambda : 1
print(f())

f2 = lambda a, b : a + b
print(f2(10, 20))

f3 = lambda a, b=20 : a + b
print(f3(10))

f4 = lambda a, *args : args
print(f4(1,2,3,4))

f5 = lambda x, **kwargs : kwargs
print(f5(1, a=10, b=20))

def fn(a, b, f):
    ret = f(a,b)
    print('fn:', ret)
    
fn(20,10, lambda a,b: a+b)
fn(20,10, lambda a,b: a-b)
fn(20,10, lambda a,b: a*b)
fn(20,10, lambda a,b: a/b)
