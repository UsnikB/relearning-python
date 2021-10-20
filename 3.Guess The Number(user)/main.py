# Computer gusses the random number decided by the User

import random

def computer_guess():
    print("Pick a number in your mind, dont tell me! The number can be ")
    from_number = int(input("from: "))
    to_number = int(input("to: "))
    responce = 'A'
    while responce != 'c':
        if from_number != to_number:
            random_number = random.randint(from_number, to_number)
        else:
            random_number = from_number

        responce = input(f'Is the number {random_number}, Too high (H), Too Low (L), or Correct (C)??: ').lower()
        if responce == 'h':
            print("High?? let me try again!!")
            to_number = random_number - 1
        elif responce == 'l':
            print("Low?? let me try again!!")
            from_number = random_number + 1
        elif responce == 'c':
            continue
        else:
            print("Invalid responce!")
            exit()

    print(f"Ohh, {random_number} was correct?? Nice")

computer_guess()
