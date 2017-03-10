import random

cnt = 1
n = random.randint(1, 100)
print "Guess the number(1~100) in 10 times."
while True:
    x = input("Insert number you guess (%d) : " % cnt)
    cnt+=1
    if cnt >= 11:
        print "You fail."
        break
    else:
        if x == n:
            print "Correct answer!"
            break
        else:
            if x > n:
                print "Lower."
            else:
                print "Higher."
    