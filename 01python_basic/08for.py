for x in [1,2,3]:
    print(x)

for x in 'abcde':
    print(x)
    
animals = ['cat', 'dog', 'elephant', 'fox']
for x in animals:
    print(x)


for i in range(len(animals)):
    print(i, 'th :', animals[i])
    
print(list(range(10)))
for i in range(10):
    print(i)


print(list(range(0,10, 1))) 
print(list(range(10,0, -1))) 
print(list(range(10,-1, -1))) 
print(list(range(5,-1, -1)))

print('-'*80)

friends = [{'name':'aaa', 'isMan' : True, }, {'name':'bbb', 'isMan':False}, {'name':'ccc', 'isMan':False}, {'name':'ddd', 'isMan':True}]
for i in friends:
    if(i['isMan'] == False):
        print("%s is not man" %i['name'])
