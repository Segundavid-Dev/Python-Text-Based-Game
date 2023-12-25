import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnnigs(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol == symbol_to_check:
                break
            else:
                winnings == values[symbol] * bet 
                winnings_lines.append(line + 1)

    return winnings,winnings_lines


def get_machine_slot(rows, cols, symbols):
    """Generate symbols that would be in each column based on the frequency of the symbol_count"""
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)

            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
     for row in range(len(columns[0])):
         for i, column in enumerate(columns):
             if i != len(columns) - 1:
                 print(column[row],end=" | ")
             else: 
                print(column[row],end='')
            
         print()


def deposit():
    """Function to collect user inputs and bets"""
    while True:
        amount = input("What would you like to deposit? $")

        #check  if amount is actually a digit
        if amount.isdigit():
            #convert amount to int type
            amount = int(amount)
            #check for amount with if condition
            if amount > 0:
                break 
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 -" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("pls enter a number")

    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:                                                                    
            print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"you are betting  ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_machine_slot(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winnings_lines = check_winnnigs(slots,lines,bet,symbol_value)
    print(f"you won {winnings}.")
    print(f"You won on lines:",*winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("Press enter to play(q to quit)")
        if answer.lower() == 'q':
            break
        balance += spin(balance)
    print(f"you left with ${balance}")
main()