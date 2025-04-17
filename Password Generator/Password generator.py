import random
import string

characters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

try:
    char_range = int(input("How many letters would you like in your password: "))
    digit_range = int(input("How many digits would you like in your password: "))
    symbol_range = int(input("How many symbols would you like in your password: "))

    password = []

    for i in range(char_range):
        password.append(random.choice(characters))
    for i in range(digit_range):
        password.append(random.choice(digits))
    for i in range(symbol_range):
        password.append(random.choice(symbols))

    random.shuffle(password)
    password = "".join(password)
    print(password)

except ValueError:
    print("Enter a valid number.")