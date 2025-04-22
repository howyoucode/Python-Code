import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

limit = 4
game_over = False

if input("Do you wanna play? (y/n) ").lower().strip() == "y":
    
    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    i = 1
    while i < limit:
        print(f"Your cards are {user_cards}")
        print(f"Computer 1st card is {computer_cards[0]}")
        user_total = sum(user_cards)
        computer_total = sum(computer_cards)

        # Blackjack check
        if user_total == 21 and len(user_cards) == 2:
            print("You won! 🎉 (Blackjack)")
            game_over = True
            break
        elif computer_total == 21 and len(computer_cards) == 2:
            print("You lose! 💀 (Computer got Blackjack)")
            game_over = True
            break
        
        # If user goes over 21, reduce Ace (11 -> 1)
        if user_total > 21 and 11 in user_cards:
            user_cards[user_cards.index(11)] = 1

        if input("Do you wanna add one more card? (y/n) ").lower().strip() != "y":
            break

        user_cards.append(random.choice(cards))
        i += 1

    if not game_over:    
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
            # Auto convert ace if total goes above 21
            if sum(computer_cards) > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
        
        print(f"\nYour final hand: {user_cards} | Total: {sum(user_cards)}")
        print(f"Computer final hand: {computer_cards} | Total: {sum(computer_cards)}")

        if sum(computer_cards) > 21:
            print("You won! 🎉 (Computer busted)")

        elif sum(user_cards) > sum(computer_cards):
            print("You won! 😎")

        elif sum(user_cards) == sum(computer_cards):
            print("It's a draw! 🤝")
            
        else:
            print("You lose! 💀")
else:
    print("Have a nice day! 👋")