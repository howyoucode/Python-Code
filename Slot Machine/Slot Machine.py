import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

cols = 3
rows = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine(cols, rows):
    # Reset the all_symbols list for each spin
    all_symbols = []
    for key, value in symbol_count.items():
        for _ in range(value):
            all_symbols.append(key)

    columns = []
    for _ in range(cols):
        column = []
        for _ in range(rows):
            current_symbols = all_symbols[:]
            value = random.choice(current_symbols)
            all_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        deposit = input("Enter the amount you want to deposit $? (x) to exit: ")
        if deposit.lower().strip() == "x":
            return None
        elif deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                return deposit
            else:
                print("Deposit must be greater than 0.")
        else:
            print("Enter a valid number.")

def get_lines():
    while True:
        lines = input(f"Enter the number of lines (1-{MAX_LINES}): (x) to exit: ")
        if lines.lower().strip() == "x":
            return None
        elif lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                return lines
            else:
                print(f"Lines must be between (1-{MAX_LINES}).")
        else:
            print("Enter a valid number.")

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? (x) to exit: ")
        if bet.lower().strip() == "x":
            return None
        elif bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between ({MIN_BET}-{MAX_BET}).")
        else:
            print("Enter a valid number.")

def evaluate_spin(columns, lines, bet):
    # Evaluate the results of the spin
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            if col[line] != symbol:
                break
        else:
            winnings += bet * 10  # Example: if all symbols are the same, multiply by 10
    return winnings

def main():
    balance = deposit()
    if balance is None:
        return
    lines = get_lines()
    if lines is None:
        return
    while True:
        bet = get_bet()
        if bet is None:
            return
        total_bet = bet * lines
        if total_bet <= balance:
            balance -= total_bet  # Deduct the total bet amount from balance before spin
            print(f"Your total bet is {total_bet}")
            columns = get_slot_machine(cols=3, rows=3)
            print_slot_machine(columns)
            winnings = evaluate_spin(columns, lines, bet)
            balance += winnings  # Add winnings to balance
            print(f"You won: {winnings}$")
            print(f"Your current balance is {balance}$")
        else:
            print(f"Insufficient funds! Your current balance is {balance}$, but you're trying to bet {total_bet}$.")

main()
