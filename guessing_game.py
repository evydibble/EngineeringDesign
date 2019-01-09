#I remade the guessing game without using any loops and only recursion

import random
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
    
def try_again():
    guess = int(input("What is your guess?"))
    if guess > number:
        print("Too High")
        try_again()
    elif guess < number:
        print("Too Low")
        try_again()
    elif guess == number:
        print("You win! The number was {}". format(number))

try_again()        
