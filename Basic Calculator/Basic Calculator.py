def operate(value1, value2, operator):
    if operator == 0:
        return value1 + value2
    if operator == 1:
        return value1 - value2
    if operator == 2:
        return value1 * value2
    if operator == 3:
        if value2 != 0:
            return value1 / value2
        else:
            print("Cannot divide by zero.")
            return value1  # Returning original value to avoid breaking the loop

print("Choose the operator by number:")
print("0 - Add")
print("1 - Subtract")
print("2 - Multiply")
print("3 - Divide")

try:
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    operator = int(input("Select operation (0-3): "))

    if 0 <= operator <= 3:
        while True:
            value1 = operate(value1, value2, operator)
            print(f"Result: {value1}")
            if input("Do you want to continue operating on the result? (y/n): ").lower().strip() == "y":
                value2 = float(input("Enter the next number: "))
                operator = int(input("Select operation (0-3): "))
                if not 0 <= operator <= 3:
                    print("Invalid operator. Exiting.")
                    break
            else:
                print("Calculation finished.")
                break
    else:
        print("Invalid operator. Please choose a number between 0 and 3.")

except ValueError:
    print("Please enter valid numeric values.")
