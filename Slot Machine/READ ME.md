# Slot Machine Game

Welcome to the Slot Machine Game! This is a simple text-based slot machine game implemented in Python. The game allows players to deposit money, choose how much to bet, and spin the slot machine in hopes of winning.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Game Logic](#game-logic)
- [Symbols](#symbols)
- [Example Gameplay](#example-gameplay)
- [License](#license)

## Features

- **Deposit Money**: Players can deposit any amount of money to start playing.
- **Choose Lines**: Bet on 1 to 3 lines.
- **Set Bet Amount**: Choose how much to bet on each line (between $1 and $100).
- **Spin the Slot Machine**: Randomly generates a result based on the symbols.
- **Winnings Calculation**: Calculate winnings based on matching symbols.
- **Current Balance Display**: Shows the current balance after each spin.
- **Quit Option**: Players can quit the game at any time.

## Requirements

To run this project, you'll need:
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```

## Usage

1. Run the game:
   ```bash
   python slot_machine.py
   ```
2. Follow the on-screen prompts to deposit money, choose your bets, and spin the slots.

## Game Logic

The game consists of the following components:

- **Deposit**: Players can deposit money to start playing.
- **Betting**: Players choose how many lines to bet on and the amount per line.
- **Slot Machine Spin**: Randomly generates a slot machine result based on the symbols and their counts.
- **Winning Check**: Calculates winnings based on the symbols that match across the selected lines.

## Symbols

- **Symbols and their counts**:
  - A: 2
  - B: 4
  - C: 6
  - D: 8

- **Symbol values**:
  - A: $5
  - B: $4
  - C: $3
  - D: $2

The winnings are calculated based on the number of symbols that match across the selected lines.

## Example Gameplay

1. Deposit an amount (e.g., $50).
2. Choose the number of lines to bet on (e.g., 2 lines).
3. Set the bet amount per line (e.g., $10).
4. Spin the slot machine.
5. Check for winnings and update the balance accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
