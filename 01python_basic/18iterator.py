class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.current < self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration()

obj = MyIterator(1, 10)
for x in obj:
    print x