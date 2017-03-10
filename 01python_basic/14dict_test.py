dict1 = {'name':'Lee','age':'27','height':185}
print type(dict1), dict1, len(dict1)
print dict1.get('name')

dict1['height'] = 180
dict1['weight'] = 68
print 'after editing:', dict1

del dict1['height']
print dict1

dict1.clear()
print dict1

dict1['new'] =123
print dict1


dict2 = {'car':'bmw','house':'aprtment','phone':'android'}
print dict2.keys()
print dict2.values()
print dict2.items()
print dict2.items()[0][0]


for key in dict2:
    value=dict2[key]
    print key, ':', value
print'--------------------'

for key in dict2.keys():
    value = dict2[key]
    print key, ':', value
