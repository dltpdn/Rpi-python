my_list = [1,2,3,4]
print my_list[0]
print my_list[-1]
print my_list[1:3]
print my_list[:3]
print my_list[1:]
print my_list[:]
print my_list[1::2]
print my_list[::2]
print my_list * 2
print my_list + [10, 20]
my_list[1] = 5
print my_list
print len(my_list)

friends = ['cat', 'dog', 'elephant', 'snake', 'flog' ]
for item in friends: 
    print item

print friends[0]
friends[1] = 1
friends.append(10)
friends.remove('snake')
del friends[3]
print friends.pop() 

for i in range(len(friends)): 
    print i, ':', friends[i]

