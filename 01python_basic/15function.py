# -*- coding:utf-8 -*-

def fn1():
    pass

fn1()

def fn2():
    print("fn2")
fn2()

def fn3(a):
    print("fn3",a)

fn3("abc")
fn3(999)

def fn4(arg1, arg2):
    print("arg1:",arg1)
    print("arg2:",arg2)

fn4("one", "two")
result1 = fn4("three", "four")
print("fn4 return :",result1)

def fn5():
    print("fn5()")
    return

def fn6():
    print("fn6()")
    return None

result2 = fn5()
result3 = fn6()
print("fn5 return:",result2)
print("fn6 return:",result3)

def getSum(num1, num2):
    result= num1+num2
    return result

print(getSum(10, 20))
f1 = getSum
print(f1(1,2))

def showSum(num1, num2):
    result = num1+num2
    print("showSum:",result)

showSum(100, 200)

def fn7(*args):
    print("fn7:", args)
    
fn7()
fn7(10)
fn7("one","two","three")
fn7(10,20,30,40,50)

def fn8(arg1, *args):
    print("fn8 arg1:",arg1)
    print("fn8 args:",args)

fn8("aaa")
fn8("aaa","bbb")
fn8("aaa","bbb","ccc")

def fn9(num=0):
    print("num:",num)

fn9()
fn9(999)

formatStr = "No:{} name:{} addr:{}".format(1, "lee", "seoul")
print(formatStr)

def fn10(num=0, name="Lee", addr="Seoul"):
    result="No:{} name:{} addr:{}".format(num, name, addr)
    print(result)

print(fn10())

def fn11(**kwargs):
    print(type(kwargs))
    print("kwargs : ",kwargs)

fn11()
fn11(num=1)
fn11(num=2,name="Park",addr="Ilsan")

def fn12(arg1, *args, **kwargs):
    print("arg1:",arg1)
    print("args:",args)
    print("kwargs",kwargs)

fn12(999)
fn12(999,"one","two","three")
fn12(999,"one","two","three",num=3,name="monkey",addr="seoul")
