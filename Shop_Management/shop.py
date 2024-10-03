from shoppass import validate_password   #To verify password requirements
import json

class Items:
    def __init__(self, item, price=0, stock=0, status="In stock"):
        self.item = item
        self.price = price
        self.stock = stock
        self.status = status

class Person(Items):
    def __init__(self, name, item, price, stock):
        super().__init__(item, price, stock)
        self.name = name

items = {}   #To store shop items, stock, item's price
borrow = {}  #To add information of person who borrowd
with open("shop_key.json", "r") as f:
    seller = json.load(f) #seller account enter key

def create_items():
    while True:
        item = input("Enter item name: ").strip().capitalize()
        if item not in items:
            while True:
                price = input("Enter item price: ").strip()
                if price.isdigit():
                    price = int(price)
                    while True:
                        stock = input("Enter stock quantity: ")
                        if stock.isdigit():
                            stock = int(stock)
                            items[item] = Items(item, price, stock)
                            return
                        else:
                            print("Enter a valid quantity (integer).")
                else:
                    print("Enter a valid price (integer).")
        else:
            print("Item already exists.")
        
def remove_items(item=""):
    if item:
        if item in items:
            del items[item]
            print("No more item available in this stock.")
            return
    while True:
        item = input("Enter item name to remove or (x) to return: ").strip().capitalize()
        if item.lower() == "x":
            return
        elif item in items:
            del items[item]
            print("Item removed successfully.")
            return
        else:
            print("Item not found in stock.")

def price_change():
    while True:
        item = input("Enter item name to update price: ").strip().capitalize()
        if item in items:
            while True:
                price = input("Enter new price: ").strip()
                if price.isdigit():
                    price = int(price)
                    items[item].price = price
                    print(f"Price updated for {item}.")
                    return
                else:
                    print("Enter a valid price (integer).")
        else:
            print("Item not found in stock.")

def block():
    while True:
        item = input("Enter item name to block or (x) to return: ").strip().capitalize()
        if item.lower() == "x":
            return
        elif item in items:
            items[item].status = "Blocked"
            print(f"{item} is now blocked.")
            return
        else:
            print("Item not found in stock.")

def buy():
    while True:
        item = input("Enter item name to purchase or Enter (x) to exist: ").strip().capitalize()
        if item == "X":
            return
        elif item in items:
            while True:
                number_of_items = input("Enter quantity to purchase: ")
                if number_of_items.isdigit():
                    number_of_items = int(number_of_items)
                    if number_of_items <= items[item].stock:
                        price = items[item].price * number_of_items
                        print(f"Total cost: ${price}.")
                        while True:
                            amount = input("Enter amount paid: ")
                            if amount.isdigit():
                                amount = int(amount)
                                if amount == price:
                                    print("Order is done.")
                                    items[item].stock -= number_of_items
                                    if items[item].stock == 0:
                                        remove_items(item)
                                    return
                                elif amount < price:
                                    left_amount = price - amount 
                                    if input(f"Amount paid: ${amount}. ${left_amount} remaining. Cancel (y) or add to borrow list (any key): ").lower() == "y":
                                        print("Order canceled.")
                                        return
                                    else:                                
                                        borrow_item(number_of_items, item, amount, left_amount)
                                        if items[item].stock == 0:
                                            remove_items(item)
                                        return
                                else:
                                    print("The amount you enter is exceeded.")
                            else:
                                print("Enter a valid amount (numeric).")
                    else:
                        print("Insufficient stock. Enter a valid quantity.")
                        if input("Show available stock (y/n): ").lower() == "y":
                            print(f"Available stock for {item}: {items[item].stock}")
                else:
                    print("Enter a valid quantity (numeric).")
        else:
            print("Item not found.")
            if input("Show available stock (y/n): ").lower() == "y":
                display_items()

def display_borrow():
    for k, v in borrow.items():
        print(f"Name: {v.name}, Item: {v.item}, Amount Owed: ${v.price}, Number of Items: {v.stock}")

def borrow_item(number_of_items=0, item="", amount=0, left_amount=0):
    while True:
        if not item:
            item = input("Enter borrowed item name: ").strip().capitalize()
        if item in items:
            number_of_items = input("Enter quantity to borrow: ")
            if number_of_items.isdigit():
                number_of_items = int(number_of_items)
                price = items[item].price * number_of_items
                amount = input("Enter amount paid: ")
                if amount.isdigit():
                    amount = int(amount)
                    if amount < price:
                        left_amount = price - amount
                        name = input("Enter borrower's name: ").strip().title()
                        if name in borrow:
                            if input("Already an account in database. Want to update? (y / n): ").lower() == "y":
                                borrow[name].item = item
                                borrow[name].price += left_amount
                                borrow[name].stock += number_of_items
                                items[item].stock -= number_of_items
                                if items[item].stock == 0:
                                    remove_items(item)
                                print("Order placed.")
                            else:
                                print("Please use a different name.")
                        else:
                            if input("Create an account (y / n): ").lower() == "y":
                                borrow[name] = Person(name, item, left_amount, number_of_items)
                                items[item].stock -= number_of_items
                                print("Order placed.")
                                if items[item].stock == 0:
                                    remove_items(item)
                            else:
                                print("Order cancelled!")
                    else:
                        print("Amount exceeded the total price.")
                else:
                    print("Enter a valid amount (integer).")
            else:
                print("Enter a valid quantity (integer).")
        else:
            print("Item not in stock!")
        return

def payment_return():
    if borrow == {}:
        return
    while True:
        name = input("Enter your name: ").strip().title()
        if name in borrow:
            person = borrow[name]
            print(f"Borrower: {person.name}, Item: {person.item}, Amount Owed: ${person.price}, Number of Items: {person.stock}")

            while True:
                amount = input("Enter payment amount: ")
                if amount.isdigit():
                    amount = int(amount)
                    if amount > person.price:
                        print("Amount exceeds balance.")
                    else:
                        person.price -= amount
                        print(f"Remaining amount to pay: ${person.price}")
                        if person.price == 0:
                            print("Payment complete. Borrow record removed.")
                            del borrow[name]
                            return
                        else:
                            if input("Do you wanna add remaining amount in borrow account? (y / n): ").lower() == "y":
                                borrow[name].price = person.price
                                return
                            else:
                                person.price += amount
                                print("Payment cancel.")
                                return
                else:
                    print("Enter a valid amount (numeric).")
        else:
            print("Name not found. Check again.")
            if input("Wanna see borrow list (y / n)") == "y":
                display_borrow()

def display_items():
    if items == {}:
        print("Nothing in stock.")
    else:
        for k, v in items.items():
            print(f"Item: {k}, Price: ${v.price}, Stock: {v.stock}, Status: {v.status}")

def options():
    while True:
        print("\n(1) Add an item.")
        print("(2) Remove an item.")
        print("(3) Change item price.")
        print("(4) Block an item.")
        print("(5) Buy an item.")
        print("(6) Borrow an item.")
        print("(7) Return payment.")
        print("(8) Show items in stock.")
        print("(9) Show borrow list.")
        print("(10) Exit the program.\n")
        choice = input("Select an option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice < 11:
                if choice == 1:
                    create_items()
                elif choice == 2:
                    remove_items()
                elif choice == 3:
                    price_change()
                elif choice == 4:
                    block()
                elif choice == 5:
                    buy()
                elif choice == 6:
                    borrow_item()
                elif choice == 7:
                    payment_return()
                elif choice == 8:
                    display_items()
                elif choice == 9:
                    display_borrow()
                elif choice == 10:
                    return
            else:
                print("Invalid choice. Try again.")
        else:
            print("Enter a valid number.")

def sell_buy():
    while True:
        seller_or_buyer = input("Are you buyer or seller? ").lower().strip()
        if seller_or_buyer == "buyer":
            buy()
        elif seller_or_buyer == "seller":
            while True:
                username = input("Enter your username or Enter (x) to exit: ").strip()
                if "x" == username.lower():
                    break
                elif username in seller:
                    while True:
                        password = input("Enter your password: ").strip()
                        if validate_password(password):
                            if password == seller[username]:
                                options()
                                return
                            else:
                                print("Password is not matched!")
                        else:
                            print("First letter should be capital, and the password must contain at least one special character and one number.")
                else:
                    print("Could not find any username.")
        else:
            print("Enter a correct option!")

while True:
    sell_buy()