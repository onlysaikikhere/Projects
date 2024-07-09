import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback=input(f"is {guess} too high (h) , too low (l) or correct (c)")
        if feedback == 'h' :
            high= guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("yay you guessed the correct number!!")

guess(1290)
