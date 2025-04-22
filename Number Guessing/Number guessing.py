import random

def get_range():
    while True:
        try:
            low_limit = int(input("Enter the starting number for the guessing range: "))
            high_limit = int(input("Enter the ending number for the guessing range: "))
            if low_limit >= high_limit:
                print("Starting number must be less than ending number.")
                continue
            return low_limit, high_limit
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_difficulty():
    while True:
        difficulty_level = input("Choose a difficulty. Type 'easy' 'medium' or 'hard': ").lower().strip()
        if difficulty_level == "easy":
            return 10
        elif difficulty_level == "medium":
            return 7
        elif difficulty_level == "hard":
            return 5
        else:
            print("Not an option. Please type 'easy', 'medium', or 'hard'.")

def play():    
    low_limit, high_limit = get_range()
    computer_guess = random.randint(low_limit, high_limit)
    attempts_left = get_difficulty()

    while attempts_left > 0:
        try:
            your_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if your_guess == computer_guess:
            print("You won!")
            break
        else:
            attempts_left -= 1
            if attempts_left != 0: 
                hint = "Too High" if attempts_left > computer_guess else "Too Low"
                print(f"{hint} You have {attempts_left} attempts remaining.")
            else:
                print(f"No more attempts. The correct number was {computer_guess}.")


print("Welcome to the Number Guessing Game!")
if input("Do you want to play (yes/no): ").lower().strip() == "y":
    while True:
        play()
        if input("Do you wanna play again ? (y/n): ").lower().strip() != "y":
            print("Thanks for playing! Goodbye.")
            break
else:
    print("Maybe next time. Have a great day!")
