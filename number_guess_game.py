import random

def guess_number(x):
    random_int = random.randint(1, x)
    people_guess = 0
    while people_guess != random_int:
        people_guess = int(input(f'Guess a number between 1 and {x}:'))

        if people_guess > random_int:
            print('too high, try again!')

        else:
            print('too low, try again!')
        
    print('Yeah, you got me! Awesome~')         
    
    
guess_number(100)