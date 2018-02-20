tuple1 = ("one","two","three")
print(tuple1)

print(tuple1[0])
#tuple1[0]="four"
#tuple1.append("four")


list1 = list(tuple1)
print(list1)

print("list1 == tuple1 : ", list1 == tuple1)

tuple2 = tuple(list1)
print(tuple2)

tuple3 = (10,)
print(type(tuple3))

tuple4 =10,20,30
print("tuple4 : ",tuple4)

num1, num2, num3=tuple4
print(num1, num2, num3)
a,b,c,d = 1,2,3,4
print(a,b,c,d)

first="girl"
second="boy"
second, first = first, second

print(first, second)
