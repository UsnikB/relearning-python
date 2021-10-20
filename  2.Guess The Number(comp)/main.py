# Guessing the random number decided by the Computer

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Worng! Too low.")
        elif guess > random_number:
            print("Worng! Too high.")
    print(f'Yaap, thats it! {random_number} is correct')

guess(5)