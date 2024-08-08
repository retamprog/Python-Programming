# here in this project we are going to simulate a Hand Cricket Game
# like we used to play during our time in childhood
# first part we will ask the user odd or eve for choosing the batter or ball
# the one who wins will get to choose bat or ball

# player1 and player2
from getpass import getpass

player1_name = input('Enter your name , player 1: ')
player2_name = input('Enter your name , player 2: ')
player1_oddeve = input('Do You Want Odd or Eve: ')

print(f'{player1_name} has choosen {player1_oddeve}')
# print('Both players be ready with your number s ')
player1_choice = int(getpass(f"{player1_name}'s choice:  "))
player2_choice = int(getpass(f"{player2_name}'s choice:  "))
player1_action1=''
player2_action2=''
if (player1_choice + player2_choice) % 2 == 0:
    if player1_oddeve == 'eve':
        print(f'{player1_name} gets to bat first ')
        player1_action = 'bat'
        player2_action = 'ball'
    else:
        print(f'{player2_name} gets to bat first ')
        player2_action = 'bat'
        player1_action = 'ball'
else:
    if player1_oddeve == 'odd':
        print(f'{player1_name} gets to bat first ')
        player1_action = 'bat'
        player2_action = 'ball'
    else:
        print(f'{player2_name} gets to bat first ')
        player1_action = 'ball'
        player2_action = 'bat'

if player1_action == 'bat' and player2_action == 'ball':
    print(f'For the first innings the batter is {player1_name} and the baller is {player2_name}')
else:
    print(f'For the first innings the batter is {player2_name} and the baller is {player1_name}')

print('Now we will start the first innings of the match ')
var= True
runs1=0

while var==True:
    if player1_action=='bat':
        # the player2 is the baller
        player1_throw=int(getpass(f'{player1_name} , your chance-> '))
        player2_throw=int(getpass(f'{player2_name} ,your chance-> '))
        if player1_throw>10 or player2_throw>10:
            print('invalid throws, run throw must be between 0-10')
            continue
        if player1_throw==player2_throw:
            print(f'{player1_name} is OUT')
            break
        else:
            runs1+=player1_throw
            print(f'{player1_name} scores {runs1}')

    else:
        player2_throw = int(getpass(f'{player2_name} , your chance-> '))
        player1_throw = int(getpass(f'{player1_name} ,your chance-> '))
        if player1_throw>10 or player2_throw>10:
            print('invalid throws, run throw must be between 0-10')
            continue
        if player1_throw == player2_throw:
            print(f'{player2_name} is OUT')
            break
        else:
            runs1 += player2_throw
            print(f'{player2_name} scores {runs1}')

print('Therefore the first innings comes to an end here ')
if player1_action=='bat':
    print(f'{player1_name} has scored {runs1} runs {player2_name} needs to  score atleast {runs1 + 1} runs to win the match ')
else:
    print(f'{player2_name} has scored {runs1} runs {player1_name} needs to  score atleast {runs1 + 1 }runs to win the match ')

print('We will now start the second innings')
if player1_action == 'bat' and player2_action == 'ball':
    player1_action='ball'
    player2_action='bat'
    print(f'For the second innings the batter is {player2_name} and the baller is {player1_name}')
else:
    player2_action = 'ball'
    player1_action = 'bat'
    print(f'For the second innings the batter is {player1_name} and the baller is {player2_name}')
runs2=0
while var==True:
    if player1_action=='bat':
        # the player2 is the baller
        player1_throw=int(getpass(f'{player1_name} , your chance-> '))
        player2_throw=int(getpass(f'{player2_name} , your chance-> '))
        if player1_throw>10 or player2_throw>10:
            print('invalid throws, run throw must be between 0-10')
            continue

        if player1_throw==player2_throw:
            print(f'{player1_name} is OUT ,{player2_name} has won the match by {runs1-runs2} runs')
            break
        else:
            runs2+=player1_throw
            if runs2 > runs1:
                print(f'{player1_name} has won the match by {runs2} runs')
                break
            print(f'{player1_name} scores {runs2}')

    else:
        player2_throw = int(getpass(f'{player2_name} , your chance-> '))
        player1_throw = int(getpass(f'{player1_name} , your chance-> '))
        if player1_throw>10 or player2_throw>10:
            print('invalid throws, run throw must be between 0-10')
            continue
        if player1_throw == player2_throw:
            print(f'{player2_name} is OUT, {player1_name} has won the match by {runs1-runs2} runs')
            break
        else:
            runs2 += player2_throw
            if runs2 > runs1:
                print(f'{player2_name} has won the match by {runs2} runs')
                break
            print(f'{player2_name} scores {runs2}')

print('therefore the second innings comes to an end ')

print('And the match ends ')




