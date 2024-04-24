# 1.Guess The Number Computer
# print('Hi,Good Morning')

"""import  random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number Between 1 And {x}: "))
        if guess <random_number:
            print('Sorry,Guess again, Toooo low')
        elif guess > random_number:
            print("Sorry,Guess again, Toooo High")

    print(f'congrats,,{random_number}')

guess(100)"""


# 2.Rock Paper Scissors

"""import random

def play():
    user=input("Enter you choice? 'r' for Rack,'p' for Paper,'s' for Scissors:\n ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return  'It\'s a Tie'

    if is_win(user,computer):
        return 'you wim'

    return 'you lost!'
def is_win(player,opponet):

    if (player =='r' and opponet == 's') or (player == 's' and opponet == 'p')\
            or (player == 'p' and opponet == 'r'):
        return True

print(play())"""

# # 3.Tic-Tac-Toe
#
# import math
# import random
#
# class Player:

