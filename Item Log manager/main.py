data = {
    "kdadg123": {"Ali": [{"item": "super", "price": 45}, {"item": "Super", "price": 30}, {"item": "daal", "price": 100}, {"item": "Papar", "price": 10}]},
    "kdadg124": {"Ahmed": [{"item": "super", "price": 50}, {"item": "Super", "price": 20}, {"item": "daal", "price": 90}, {"item": "Papar", "price": 15}]},
    "kdadg125": {"Sara": [{"item": "super", "price": 60}, {"item": "Super", "price": 25}, {"item": "daal", "price": 80}, {"item": "Papar", "price": 20}]},
    "kdadg126": {"Ali": [{"item": "super", "price": 20}, {"item": "Super", "price": 15}, {"item": "daal", "price": 10}, {"item": "Papar", "price": 5}]},
}
# Shop Borrow Data Management System


def enter_data():
    try:
        name = input("Enter customer name: ").capitalize().strip()
        item = input("Enter item name: ").strip()
        price = float(input("Enter item price: "))
        return name, item, price
    except ValueError:
        print("❌ Invalid input. Please enter correct values.")
        return None, None, None


def store_data():
    name, item, price = enter_data()
    if not name or not item:
        return

    matching_ids = []
    for user_id, user_data in data.items():
        if name in user_data:
            matching_ids.append(user_id)

    if len(matching_ids) > 1:
        print("⚠ Multiple entries found. Data will be added to the first match.")
        user_id = matching_ids[0]
    elif len(matching_ids) == 1:
        user_id = matching_ids[0]
    else:
        user_id = f"kdadg{len(data) + 123}"
        data[user_id] = {name: []}

    data[user_id][name].append({"item": item, "price": price})
    print(f"✅ Entry saved for {name} under ID: {user_id}")


def details():
    name = input("Enter customer name to view details: ").capitalize().strip()
    matching_ids = [uid for uid, record in data.items() if name in record]

    if not matching_ids:
        print("❌ No records found.")
        return

    def print_record(uid):
        person = data[uid]
        records = person[name]
        total = 0
        print(f"\n🧾 Record for ID: {uid}")
        for entry in records:
            print(f"- {entry['item']} : {entry['price']}")
            total += entry["price"]
        print("🔢 Total:", total, "\n")

    if len(matching_ids) > 1:
        print("\nMultiple records found:")
        for uid in matching_ids:
            print(f"→ {uid}")
        while True:
            choice = input("Enter specific ID, 'all' to view all, or 'x' to exit: ").strip().lower()
            if choice == "x":
                break
            elif choice == "all":
                for uid in matching_ids:
                    print_record(uid)
                break
            elif choice in matching_ids:
                print_record(choice)
                break
            else:
                print("❌ Invalid input.")
    else:
        print_record(matching_ids[0])


# -----------------------------
# Main Menu
# -----------------------------
while True:
    print("\n📋 Shop Borrow Management System")
    print("1. Add New Entry")
    print("2. View Customer Details")
    print("x. Exit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        store_data()
    elif choice == "2":
        details()
    elif choice == "x":
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
