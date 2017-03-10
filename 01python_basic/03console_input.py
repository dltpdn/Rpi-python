input1 = raw_input() #abc
input2 = raw_input() # 123
print input1, type(input1), input2, type(input2)  #all str

input3 = input() #'abc' #error
input4 = input() #123
print input3, type(input3), input4, type(input4) #str, int

input5 = raw_input("Insert your name.") #Lee
input6 = input('Insert your age.') #27
print 'You are %s and %d years old.' % (input5, input6)