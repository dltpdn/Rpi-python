var1 = 'global-1'
var2 = 'global-2'
var3 = 'global-3'
def fn1():
    global var3
    var1 = 'local'
    var3 = 'local2'
    print 'var1 :', var1
    print 'var2 :', var2
    print 'var3 :', var3
fn1()    
print '-------------------'
print 'var1 :', var1
print 'var2 :', var2
print 'var3 :', var3
