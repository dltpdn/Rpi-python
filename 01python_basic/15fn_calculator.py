
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def str2num(str_val):
    if str_val.isdigit() :
        return int(str_val)
    elif str_val.replace('.', '', 1).isdigit():
        return float(str_val)
    else:
        return 0

def shell():
    operators = {'+' : plus, '-':minus, '*':multiply, '/':divide}
    print "Calculator is ready.('q' to quit)"
    while True:
        isDone = False
        line = raw_input("> ")
        line.strip()
        if 'q' in line :
            break
        for op in operators.keys():
            op_idx = line.find(op)
            if op_idx > 0 and op_idx < len(line)-1:
                fn = operators[op]
                a = str2num(line[:op_idx])
                b = str2num(line[op_idx+1:])
                print line , '=', fn(a,b)
                isDone = True
                break
        if not isDone :
            print 'Invalid expression, Try again.'
    

shell()
    