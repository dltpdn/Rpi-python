val = eval(input('Insert a digit:'))
print('the value you inserted ', val)


try:
    val = eval(input('Insert a digit again:'))
    print('the value you inserted ', val)
except Exception as e:
    print('error: %s' % e)
print('end of program')