import random

def guess(x:int):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) 
        if guess < random_number:
            print('The number is too low.')
        elif guess > random_number:
            print('The number is too high.')
        else:
            print(f'yay!! you won the game, the number was {random_number}')
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != 'high':
            guess = random.randint(low,high)
        else:
            guess = low
            
        
        feedback = input(f"Is {guess} secret number too high (H), too low (L), or correct (C)???  ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
    print(f'yaya!you win {guess}')
    
            
computer_guess(10)