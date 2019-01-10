import random
n = random.randint(0, 100)
guess = int(raw_input("Chose a number from 0-100: "))
while n != "guess":
    print
    if guess < n:
        print "try a higher number"
        guess = int(raw_input("Chose a number from 0-100: "))
    elif guess > n:
        print "try a lower number"
        guess = int(raw_input("Chose a number from 0-100: "))
    else:
        print "that's correct!"
        break
    print
