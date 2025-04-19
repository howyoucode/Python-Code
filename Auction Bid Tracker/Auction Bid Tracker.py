import os

total_bid = {}
highest = 0
winners = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        name = input("Enter your name: ").capitalize().strip()
        if not name.isalpha():
            print("Name must contain only letters.")
            continue
        bid = int(input("Enter your bid $: "))

        total_bid.update({name: bid})
        add_more = input("Do you want to add more bids? (y/n): ").lower().strip()
        if add_more != "y":
            break
        clear_screen()
    except ValueError:
        print("Please enter a valid number for the bid.")

# Determine the highest bid and identify all the winners
for name, bid in total_bid.items():
    if bid > highest:
        winners = [f"{name} with a bid of ${bid}"]
        highest = bid
    elif bid == highest:
        winners.append(f"{name} with a bid of ${bid}")

# Display the result
print("\n🏆 The Highest Bidder(s):")
if len(winners) == 1:
    print(f"🎉 {winners[0]} is the winner!")
else:
    print("🎉 We have a tie between:")
    for winner in winners:
        print(f"- {winner}")
