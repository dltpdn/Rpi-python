import m1

def greeting():
    print "this is %s's greeting." % __name__


if __name__ == "__main__":
    print "this is m2 as a top level"
    m1.greeting()