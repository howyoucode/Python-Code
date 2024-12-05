import random
import time

def generate_problem(number_range, operators):
    left = random.randint(1, number_range)
    right = random.randint(1, number_range)
    operator = random.choice(operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

def working(number_range, problem_range, operators):
    input("Are you ready? Press Enter to start the quiz!")
    print("\nSolve as quickly as you can. Good luck!")
    time_start = time.time()
    score = 0

    for i in range(1, problem_range + 1):
        expr, answer = generate_problem(number_range, operators)
        while True:
            try:
                guess = int(input(f"Problem #{i}: {expr} = "))
                if guess == answer:
                    print("Correct!\n")
                    score += 1
                    break
                else:
                    print("Incorrect! Try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    time_end = time.time()
    total_time = round(time_end - time_start, 2)
    average_time = round(total_time / problem_range, 2)

    print(f"\nQuiz Complete! Here are your results:")
    print(f"Score: {score}/{problem_range}")
    print(f"Total Time: {total_time} seconds ({round(total_time / 60, 2)} minutes)")
    print(f"Average Time per Problem: {average_time} seconds")

def main():
    print("Welcome to the Math Speed Challenge!\n")

    while True:
        try:
            number_range = int(input("Enter the maximum range for numbers (e.g., 10, 100): ").strip())
            if number_range <= 0:
                print("Range must be a positive number. Try again.")
                continue

            problem_range = int(input("Enter the number of problems you want to solve: ").strip())
            if problem_range <= 0:
                print("Number of problems must be greater than 0. Try again.")
                continue

            operator_choice = input("Choose operators (+, -, *). Enter your choices separated by spaces: ").strip()
            operators = operator_choice.split()
            if not set(operators).issubset({"+", "-", "*"}):
                print("Invalid operators! Choose from +, -, *.")
                continue

            print("\nGreat! Let's start the quiz.")
            working(number_range, problem_range, operators)
            break

        except ValueError:
            print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":
    main()
