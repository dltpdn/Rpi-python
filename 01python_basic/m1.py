import m2

def greeting():
    print("This is %s's greeting." % __name__)


if __name__ == '__main__':
    print("This is m1 as a top level.")
    m2.greeting()
    