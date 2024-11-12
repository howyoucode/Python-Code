import random 

def asking():
    while True:
        print("Welcome to Hangman game!")
        if input("DO you wanna play (y / n): ") not in ["yes", "y"]:
            print("See ya! Come again.")
            quit()
        else:
            print("Lets Go.")
            playing()

def playing():
    secret_words = ["apple", "banana", "mango", "apricot", "avocado", "grape", "strawberry", "pineapple", "cherry", "kiwi", "melon", "fig", "papaya"]
    secret_words = [i.lower() for i in secret_words]
    word = random.choice(secret_words)
    dashes = "_" * len(word)
    print(dashes)

    chances = len(word) + 2
    while True:
        if chances == 0:
            print(f"You lose! The correct word was {word}")
            return
        letter = input("Enter the single character of guessing word: ").lower()
        if len(letter) != 1:
            continue
        if letter in word:
            idx = 0
            idx_2 = []
            for i in word:
                if i == letter:
                    idx_2.append(idx)
                idx += 1
            dashes = list(dashes)
            for i in idx_2:
                dashes[i] = letter
            dashes = "".join(dashes)
            if "_" not in dashes:
                print("You won")
                return
            print(dashes, "you have", chances, "more chances.")
        else:
            chances -= 1
            print("Wrong answer! You have left", chances, "more chances.")
        


asking()