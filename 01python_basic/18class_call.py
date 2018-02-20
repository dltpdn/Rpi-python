class Callable:
    def __call__(self):
        print("__call__")

obj = Callable()
obj()


class MyDecorator:
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self):
        print('before calling %s' % self.fn.__name__)
        self.fn()
        print('after calling %s' % self.fn.__name__)

def fn():
    print('this is fn.')

fn = MyDecorator(fn)
fn()

@MyDecorator
def fn2():
    print('this is fn2')
fn2()