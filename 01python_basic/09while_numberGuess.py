import random

success = False
cnt = 1
x = random.randint(1, 100)
print("Guess the number(1~100) in 10 times.")


while cnt <= 10:
    n = eval(input("Enter the number you guess (%d) : " % cnt))
    if n <0 or n > 100 :
        print("Enter a number between 0 and 100.")
        continue
    cnt+=1
    if x == n:
        success = True
        break
    elif x > n:
        print("Higher.")
    else:
        print("Lower.")

if success:
    print("Correct answer")
else :
    print("You failed. The number is %d" % x)