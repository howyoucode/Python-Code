import random


def main():
    username = input("Enter your name: ").strip().capitalize()
    print(f"Welcome, {username}!")
    stats = {"won": 0, "lost": 0}

    while True:
        if not play_prompt(username):
            print("Thanks for playing! See you next time!")
            break
        play_game(stats)
        print(f"\nScoreboard: Wins - {stats['won']}, Losses - {stats['lost']}")


def play_prompt(username):
    while True:
        response = input("\nDo you want to play? (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def play_game(stats):
    words = [
        "rainbow", "computer", "science", "programming",
        "python", "mathematics", "player", "condition",
        "reverse", "water", "board", "geeks"
    ]
    pick_word = random.choice(words)
    guessed_word = ["_" for _ in pick_word]
    guessed_letters = set()
    chances = 5

    print("\nLet's begin!")
    print(" ".join(guessed_word))

    while chances > 0:
        guess = input("\nEnter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single alphabetic character.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in pick_word:
            guessed_word = [
                guess if pick_word[i] == guess else guessed_word[i]
                for i in range(len(pick_word))
            ]
            print("Correct guess!")
        else:
            chances -= 1
            print(f"Wrong guess! You have {chances} chance{'s' if chances != 1 else ''} left.")

        print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word correctly!")
            stats["won"] += 1
            return

    print(f"\nGame Over! The word was '{pick_word}'. Better luck next time!")
    stats["lost"] += 1


if __name__ == "__main__":
    main()
