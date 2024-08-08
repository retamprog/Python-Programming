# Project No 2- Pig Dice Game
#  Description Of the Pig Dice Game
# Pig is a simple dice game first described in print by
# John Scarne in 1945. Players take turns to roll a single die as many times as they wish, adding all roll results
# to a running total, but losing their gained score for the turn if they roll a 1.
import random


def _disclaimer():
    # this function will print the tutorial on how to play the game if the user wants.
    print('''
    Here is a disclaimer on how to play the game--->
    Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
    
    * If the player rolls a 1, they score nothing and it becomes the next player's turn. 
    * If the player rolls any other number, it is added to their turn total and the player's turn continues. 
    * If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn. 
    The first player to score 100 or more points wins. 
    
    For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, 
    but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. 
    Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-6, 
    after which she chooses to hold, and adds her turn total of 23 points to her score.
    ''')


def _roll():
    # this will be actually a random number generator which will generate a number between 1 to 6 like rolling a die.
    max_value = 6
    min_value = 1
    roll = random.randint(min_value, max_value)
    return roll


# now we are going to input the number of players who are going to play , setting the min to 2 and max to 4
while True:
    players = input("Enter the number of players who want to play (2-4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('The numbers of players must be within the range,Try again ')
    else:
        print('Invalid Input,Try again ')
max_score = 50
while True:
    tutorial = input('Do you want a tutorial on how to play the game(Y/N) ').lower()
    if tutorial == 'y':
        _disclaimer()
        break
    elif tutorial == 'n':
        print("ok, you can continue with the game")
        break
    else:
        print('Invalid choice,type y/n ')

players_score = [0 for _ in range(players)]
# now we are going to create the simulation part of the game
print('--------- Starting the game--------------')
while max(players_score) < max_score:

    for player_idx in range(players):
        current_score = 0
        while True:
            turn = input(f"It is Player{player_idx + 1}'s turn,Do you want to roll or hold(r->roll) ").lower()
            if turn == 'r':
                value = _roll()
                if value == 1:
                    print('Oops,you have rolled a 1, you are done with your turns ')
                    current_score = 0
                    break
                else:
                    print(f"Player{player_idx + 1} has rolled a: {value}")
                    current_score += value

            else:
                break
        players_score[player_idx] += current_score

        print(f"Player{player_idx + 1}'s current turn score is", current_score)
        print(f"Player{player_idx + 1}'s total score is", players_score[player_idx],'\n')
        if players_score[player_idx]>max_score:
            break


maxscore=max(players_score)
winner = players_score.index(maxscore)

print(f"Player{winner+1} has won the game ")
