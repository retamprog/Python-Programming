# project 4- Text based Slot Machine.
# its working principle is same as the ones found in a casino
# here we will ask the user to deposit the money ,
# then ask him to bet on any one or multiple lines(pay lines) of the slot machine.
# for simplicity purposes we will only keep three pay lines
# if the bet matches any of the lines ,
# then the value of the line will be multiplied with the bet and added to the balance,
# for further betting until the user wants to cash out his balance or they lose all their money.
import random as rd

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
symbols_dict = {
    "🤣": 3,
    "😍": 8,
    "😒": 2,
    "😘": 3
}
symbols_value = {
    "🤣": 5,
    "😍": 2,
    "😒": 10,
    "😘": 5
}
ROWS = 3
COLS = 3


# first we will ask the user to enter the deposit amount
def deposit():
    while True:
        amount = input("Enter the amount you want deposit: $")

        if amount.isdigit():
            amount = int(amount)
            if amount >= 10:
                break
            else:
                print('The amount must be greater than or equal to $10')
        else:
            print('Please enter valid amount')

    return amount


# the below function inputs the no of pay lines the user wants to bet on, ranging from (1-3)
def get_no_of_lines():
    while True:
        lines = input(f"Enter the no of lines you want to bet on (1-{MAX_LINES})- ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'The no of lines must be within (1-{MAX_LINES})')
        else:
            print('Please enter valid no of lines')

    return lines


#the below function will calc the amount the user wants to bet on each line
def getbet():
    while True:
        amount = input("Enter the amount you want to bet on each line- ")

        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_BET:
                break
            else:
                print(f'The no of bet must be within (${MIN_BET}-${MAX_BET})')
        else:
            print('Please enter valid bet')

    return amount


# now we will create the function which will roll the slot machine or to say will create the combinations of symbols.
def roll_slot_machine(rows, cols, symbols_dict):
    # first we will have to transfer the symbol_dict into a list of the elements that are going to be the content of the reels
    symbols = []
    for key, value in symbols_dict.items():
        for _ in range(value):
            symbols.append(key)
    # Now in this column list we are store the values of each reel in a single roll of the slot machine
    columns = []
    for _ in range(cols):
        column = []
        symbol_list = symbols.copy()
        for _ in range(rows):
            choice = rd.choice(symbol_list)
            column.append(choice)
            symbol_list.remove(choice)
        columns.append(column)
    # now this returns the value of each reel in the form of a matrix where the rows of the matrix represent the reels values
    return columns


# the below function will print the slot machine in our desired slot machine looking manner

def print_slot_machine(columns):
    # now here we will print the values of the reel as
    # it should have appeared in the slot machine with the cols showing the reel values
    # what we have to do is actually print the transpose of the matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end='')
        print()


def check_winnings(lines, total_bet, columns, value):
    #     this function will actually check whether you have a winning match and return the winnings
    winnings = 0
    winning_lines = []
    # win=True
    for line in range(lines):
        # it is the first symbol to check considering there will be least one reel
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                # win=False
                break
        else:
            winning_lines.append(line + 1)
            winnings += value[symbol] * total_bet

    return winnings, winning_lines


def spin(balance):
    lines = get_no_of_lines()

    # now here we will check whether the bet is exceeding the balance
    while True:
        bet = getbet()
        total_bet = lines * bet
        if total_bet <= balance:
            print(f"the bet per line is ${bet}, The total bet is ${total_bet}")
            break
        else:
            print('Sorry your bet exceeds your balance, current balance ' + str(balance))

    slot = roll_slot_machine(ROWS, COLS, symbols_dict)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(lines, total_bet, slot, symbols_value)
    if winnings == 0:
        print(f'you lost ${total_bet} from your current balance')
    else:
        print(f'You won ${winnings}')
        print(f'You won the lines-', *winning_lines)

    return winnings - total_bet


def ticket(balance):
    print(f'Your current balance is ${balance}')
    print('Please go to counter to cash out your balance')
    print('Come again ,Thank You')
    quit()


# we will create a main function which will call all the remaining functions
def main():
    balance = deposit()
    while True:
        balance += spin(balance)
        if balance == 0:
            print('You have 0 balance,please reload your balance')
            balance = deposit()

        print(f'your current balance ${balance}')
        want_to_cash_out = input("Do you want to cash out or not (Y/N) ").lower()
        if want_to_cash_out == 'y':
            ticket(balance)
        else:
            print('Play Again')


main()
