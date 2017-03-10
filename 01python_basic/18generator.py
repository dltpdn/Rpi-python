def generator():
    cnt = 0
    while cnt<10:
        yield cnt
        cnt+= 1

for x in generator():
    print x