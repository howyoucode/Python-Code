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



# OR

"""

import random

fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple", "Grapes", "Watermelon", "Papaya", "Strawberry", "Blueberry", "Kiwi", "Pomegranate", "Cherry", "Peach", "Pear", "Plum", "Guava", "Lychee", "Coconut", "Avocado"]

fruits = [fruit.lower() for fruit in fruits]

random_word = random.choice(fruits)
length = len(random_word)
life = 5
guess = []
print("Lets Start the game!")
blanks = ["_"] * length
print(" ".join(blanks))


while True:
    user_input = input("Enter the letter: ").lower().strip()
    if len(user_input) == 1:
        if user_input.isalpha():
            if user_input not in guess:
                guess.append(user_input)
                if user_input in random_word:
                    for idx, char in enumerate(random_word):
                        if char == user_input:
                            blanks[idx] = user_input
                    print(" ".join(blanks))
                    if "_" not in blanks:
                        print("You win")
                        break
                else:
                    print(" ".join(blanks))
                    print("Wrong")
                    life -= 1
                    if life == 0:
                        print("You lose.")
                        break
            else:
                print("You already guessed it.")

        else:
            print("Character must be an alphabetic.")
    else:
        print("Enter a single character.")

"""