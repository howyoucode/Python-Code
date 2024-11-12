# Hangman Game

This is a simple Python implementation of the Hangman game. The game allows the player to guess letters of a secret word until they either guess the word correctly or run out of chances.

## How to Play
1. The game will ask if you want to play. Type `y` or `yes` to play.
2. You will be shown a word with underscores representing the letters.
3. Guess one letter at a time. If the letter is in the word, it will replace the underscore in the word.
4. You have a limited number of chances to guess wrong letters. The number of chances is equal to the length of the word + 2.
5. If you guess the word before running out of chances, you win the game.
6. If you run out of chances, the game will show the correct word and you lose.

## Code Explanation

### Asking Function
The `asking()` function:
- Greets the player and asks if they want to play.
- If the player types `y` or `yes`, the game starts by calling the `playing()` function.
- If the player types anything else, the game exits.

### Playing Function
The `playing()` function:
- Selects a random word from a predefined list of fruits.
- The word is displayed as underscores.
- The player is given a certain number of chances to guess the word.
- If the player guesses a letter correctly, the word is updated with the guessed letter.
- If the player guesses wrong, the number of chances decreases.
