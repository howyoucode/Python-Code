from password-verification import validate_password

class Account:
    def __init__(self, account, password, deposit):
        self.account = account
        self.__password = password
        self.deposit = deposit

    @property
    def details(self):
            return str(f"The amount in your account is {str(self.deposit)} and your account number is {str(self.account)}.")
        
    def debit(self, amount):
        if self.deposit < amount:
            print("Print not enough money for debit.")
        else:
            self.deposit -= amount
            print(f"{amount} debit amount has been done.")


    def credit(self, amount):
         self.deposit += amount
         print(f"{amount} credit amount has been done.")

accounts = {}

def create_account():
    while True:
        account = input("Enter your account number. It should be between 6 and 12 digits long: ")
        if account.isdigit() and (5 < len(account) < 13):
            if account not in accounts:
                while True:
                    password = input("Enter your password: ")
                    if validate_password(password):  # Validate password using the imported function
                        while True:
                            deposit = input("Enter your deposit amount in numeric numbers: ")
                            if deposit.isdigit():
                                deposit = int(deposit)
                                if deposit > 0:
                                    accounts[account] = Account(account, password, deposit)
                                    return
                                else:
                                    print("Deposit amount should be at least 1 dollar.")
                            else:
                                print("Enter a valid deposit amount.")
                    else:
                        print("First letter should be capital, and the password must contain at least one special character and one number.")
            else:
                print("Account already exists, try another.")
        else:
            print("Account number should be between 6 and 12 digits.")


def access_account():
    if accounts == {}:
        print("Not an account in database please add your account")
        return
    while True:
        account = (input("Enter your account number. It should be between 6 and 12 digits long: "))
        if (account.isdigit() and (len(account) > 5 and len(account) < 13)):
            account = str(account)
            if account in accounts:
                while True:
                    password = input("Enter password: ")
                    if password.isdigit():
                        password = str(password)
                        account = accounts[account]
                        if password == account._Account__password:
                            print("Access granted")      
                            option(account)
                            return
                        else:
                            print("Password is wrong!")
                    else:
                        print("Please enter numeric password.")
            else:
                print("Account not found!")

def option(account):
    while True:
        print("Enter x to exist")
        choice = input("Choose 'd' to debit 'c' to credit. For details 'details': ").lower()
        if choice == "x":
            break
        elif choice == "d":
            amount = int(input("Enter your debit amount: "))
            account.debit(amount)
        elif choice == "c":
            amount = int(input("Enter your credit amount: "))
            account.credit(amount)
        elif choice == "details":
            print(account.details)

while True:
    print("Choose options")
    print("1. Create account.")
    print("2. Access account.")
    print("3. Exit.")
    
    choice = int(input("Enter number to choose option: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        access_account()
    elif choice == 3:
        break
    else:
        print("Not an option. Choose between 1 to 3.")
