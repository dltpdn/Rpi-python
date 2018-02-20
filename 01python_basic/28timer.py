import threading

def fn():
    print("fn called")

timer = threading.Timer(5, fn)
print('ready to start timer')
timer.start()

cnt = 0
def interval():
    global cnt
    print('timer cnt :', cnt)
    if cnt <10:
        threading.Timer(1, interval).start()
    cnt+= 1    
interval()