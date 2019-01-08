import random
number = random.randint(1,17)
win = False
print ("I'm thinking of a number between 1 and 17")
while not win:
    guess = int(input("What is your guess?"))
    if guess == number:
        win = True
        print("You're right!")
    elif guess < number:
        print ("Guess higher")
    elif guess > number:
        print ("Guess lower")
print("You win! The number was {}". format(number))
