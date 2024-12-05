import random

def play(players_score, max_score):
    while max(players_score) < max_score:
        for player_idx, name in zip(range(players_no), players_name):
            current_score = 0
            print(f"\nplayer {name} Your total score is now {players_score[player_idx]}.")
            while True:
                should_roll = input(f"\nDo you wanna roll player {name}: ").lower()
                if should_roll == "y":
                    roll = random.randint(1, 6)
                    if roll == 1:
                        players_score[player_idx] = 0
                        print(f"Your total score is now 0 :(")
                        break
                    else:
                        print(f"You rolled a {roll}.")
                        current_score += roll
                        print(f"Your current score is now {current_score}.")
                elif should_roll == "n":
                    print("Okay")
                    players_score[player_idx] += current_score
                    break
                else:
                    print("Not an option. Type (y / n).")
                    continue

print("Welcome!")
while True:
    user_input = input("Do you wanna play? (y / n): ").lower() 
    if user_input == "y":
        while True:
            players_no = input("How many players wants to play (2 - 4): ")
            if players_no.isdigit():
                players_no = int(players_no)
                players_name = [input("Enter your name: ").capitalize() for i in range(players_no)]
                if 2 <= players_no <= 4:
                    players_score = [0 for _ in range(players_no)]
                    while True:
                        max_score = input("Enter the max limit you want to set: ")
                        if max_score.isdigit():
                            max_score = int(max_score)
                            play(players_score, max_score)
                            break
                        else:
                            print("Enter a number e.g. 1, 4, 7 etc.")
                    break
                else:
                    print("Enter between 2 to 4.")
            else:
                print("Enter a number e.g. 1, 4, 7 etc.")
    elif user_input == "n":
        print("Okay! Bye.")
        break
    else:
        print("Not an option.")