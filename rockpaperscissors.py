import random

def play():
    user = input("'r' for rock , 'p' for paper and 's' for stone")
    computer = random.choice(['r','p','s'])
    print(f'computer chose {computer}')
    if user == computer:
        return("Tie")
    elif (user == 'r'and computer == 's' ) or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return ('you won')
    else:
        return("you lost")
    
print(play())
