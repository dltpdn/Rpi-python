a_list = [1,5,3,4]
print [x+1 for x in a_list]
print [x for x in range(1,11) if x%2==0]
print [x for x in range(1,11) if x%2!=0]

s= [ x**2 for x in range(10)]
v= [ 2**x for x in range(13)]
m = [x for x in s if x%2 == 0]
print "S", s
print "V", v
print "M", m

a_set = set(range(10))
print {x**2 for x in a_set}


a_dict = {'a' : 10, 'b': 20, 'c': 30}
print {value:key for key, value in a_dict.items()}