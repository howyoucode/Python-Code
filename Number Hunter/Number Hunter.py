import random


def main():
    username = input("Enter your name: ").strip().capitalize()
    print(f"Welcome, {username}!")
    
    while True:
        if not play_prompt(username):
            print("See ya! Come again.")
            break
        play_game(username)


def play_prompt(username):
    """Ask if the user wants to play the game."""
    response = input(f"\nDo you want to play, {username}? (y to play, any other key to exit): ").strip().lower()
    return response == "y"


def play_game(username):
    """Main game logic."""
    chances = 5
    won, lost = 0, 0

    # Get a valid range limit from the user
    range_limit = get_range_limit()
    secret_number = str(random.randint(1000, range_limit))
    guessed_number = ["_" for _ in secret_number]

    print("\nYour secret number:")
    print(" ".join(guessed_number))

    while chances > 0:
        guess = input("\nEnter a single-digit guess: ").strip()

        # Validate input
        if not guess.isdigit() or len(guess) != 1:
            print("Invalid input. Please enter a single digit.")
            continue

        # Check if the guess is correct
        if guess in secret_number:
            guessed_number = [
                guess if secret_number[i] == guess else guessed_number[i]
                for i in range(len(secret_number))
            ]
            print("\nCorrect guess!")
            print(" ".join(guessed_number))

            if "_" not in guessed_number:
                print(f"\nCongratulations, {username}! You guessed the number: {secret_number}")
                won += 1
                break
        else:
            chances -= 1
            print(f"\nWrong guess! You have {chances} chance{'s' if chances != 1 else ''} left.")

    if "_" in guessed_number:
        print(f"\nYou lost, {username}! The number was: {secret_number}")
        lost += 1

    print(f"\nScoreboard: Wins - {won}, Losses - {lost}")


def get_range_limit():
    """Get a valid range limit from the user."""
    while True:
        range_input = input("\nEnter a range limit (must be greater than 2000): ").strip()
        if range_input.isdigit() and int(range_input) > 2000:
            return int(range_input)
        print("Invalid input. Please enter a number greater than 2000.")


# Start the program
if __name__ == "__main__":
    main()
