data = {
    "kdadg123": {"Ali": {"super": 45, "Super": 30, "daal": 100, "Papar": 10}},
    "kdadg124": {"Ahmed": {"super": 50, "Super": 20, "daal": 90, "Papar": 15}},
    "kdadg125": {"Sara": {"super": 60, "Super": 25, "daal": 80, "Papar": 20}},
    "kdadg126": {"Ali": {"super": 20, "Super": 15, "daal": 10, "Papar": 5}},
}
# Shop Borrow Data Management System

def enter_data():
    try:
        name = input("Enter customer name: ").capitalize().strip()
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid input. Please enter a valid price.")
    
    return name, item, price

# Under Develop 
def store_data():
    name, item, price = enter_data()
    if name in data:
        data.update([name][{item:price}]) # Error
    else:
        data[name] = {item:price}

def details():
    Total = 0
    found = False
    total_person = []
    name = input("Enter the customer name to search: ").capitalize().strip()
    for user_id, user_data in data.items():

        # print(person_dict)  # Debug: print person_dict
        for person_name, items in user_data.items():
            if person_name.lower() == name.lower():
                found = True
                total_person.append(user_id)

    if not found:
        print("No records found.")
        return

    if len(total_person) > 1:
        print("\nMultiple records found for this name:")
        for user_id in total_person:
            print("ID:", user_id, "Name:", name)

        while True:
            option = input("Enter a specific ID to view, type 'all' to view all records, or 'x' to go back: ")
            if option.lower() == "x":
                return
            elif option.lower() == "all":
                for user_id in total_person:
                    person = data[user_id]

                    for name, items in person.items():
                        for item, price in items.items():
                            print(f"{item} - {price}")
                            Total += price
                        print("\n░▒▓█►─═  Total Amount ═─◄█▓▒░:", Total, "\n")
                        Total = 0
                
                return

            elif option in total_person:
                person = data[option]
                for name, items in person.items():
                    for item, price in items.items():
                        print(f"{item} - {price}")
                        Total += price
                    print("\n░▒▓█►─═  Total Amount ═─◄█▓▒░:", Total, "\n")
                    Total = 0
                return
            else:
                print("Invalid ID. Please try again.")
                return

    elif len(total_person) == 1:
        print("\nSingle record found:")
        print("ID:", user_id, "Name:", name)
        person = data[total_person[0]]

        for name, items in person.items():
            for item_name, price in items.items():
                print(f"{item_name} - {price}")
                Total += price
            print("\n░▒▓█►─═  Total Amount ═─◄█▓▒░:", Total, "\n")
            Total = 0


while True:
    select_option = input("Select an option (1: Add Entry, 2: View Details, x: Exit): ")
    if select_option == "x":
        break
    elif select_option == "1":
        store_data()
    elif select_option == "2":
        details()
    elif select_option == "3":
        pass
    elif select_option == "4":
        pass
    else:
        print("Invalid option selected. Please try again.")
