import random

# Sample dataset (name and follower count in millions)
data = [
    {"name": "Cristiano Ronaldo", "followers": 630},
    {"name": "Lionel Messi", "followers": 520},
    {"name": "Kylie Jenner", "followers": 400},
    {"name": "Dwayne Johnson", "followers": 390},
    {"name": "Selena Gomez", "followers": 420},
    {"name": "Taylor Swift", "followers": 280},
    {"name": "Ariana Grande", "followers": 380},
    {"name": "MrBeast", "followers": 250},
    {"name": "Kim Kardashian", "followers": 360},
    {"name": "Beyoncé", "followers": 320}
]

def format_account(account):
    return f"{account['name']}"

def get_random_account(exclude=None):
    account = random.choice(data)
    while exclude and account == exclude:
        account = random.choice(data)
    return account

def higher_lower_game():
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account(exclude=account_a)

    while game_should_continue:
        print(f"\n🔸Compare A: {format_account(account_a)}")
        print("    VS")
        print(f"🔹Compare B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        a_followers = account_a["followers"]
        b_followers = account_b["followers"]

        if (guess == "A" and a_followers > b_followers) or (guess == "B" and b_followers > a_followers):
            score += 1
            print(f"Correct! Your score: {score}")
            account_a = account_b
            account_b = get_random_account(exclude=account_a)
        else:
            print(f"Wrong! Final score: {score}")
            game_should_continue = False

# Start the game
higher_lower_game()
