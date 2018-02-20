class A:
    def method(self):
        print('method of A')
class B:
    def method(self):
        print('method of B')
class C(A, B):
    pass

obj = C()
obj.method()