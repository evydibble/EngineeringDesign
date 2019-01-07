import random
number = random.randint(1,10)
win = False
print ("I'm thinking of a number between 1 and 10")
while not win:
    guess = int(input("What is your quess?"))
    if guess == number:
        win = True
        print("You're right!")
    elif guess < number:
        print ("Guess higher")
    elif guess > number:
        print ("Guess lower")
print("You win! The number was {}". format(number))
