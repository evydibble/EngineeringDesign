#I remade the guessing game without using any loops

import random
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 10")

def too_Low():
    print("Too Low!")
    try_again()
    
def too_High():
    print("Too High!")
    try_again()

def win():
    print("You win! The number was {}". format(number))
    
def try_again():
    guess = int(input("What is your guess?"))
    if guess > number:
        too_High()
    elif guess < number:
        too_Low()
    elif guess == number:
        win()

try_again()        
