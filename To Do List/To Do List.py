import json
tasks = {}
filenames = [] 
def option():
    while True:
        print(f"File names: {filenames}")
        print("(1) Add Task.")
        print("(2) View Task.")
        print("(3) Mark/Unmark Task.")
        print("(4) Delete Task.")
        print("(5) Save Task.")
        print("(6) Load Task.")
        print("(7) Exit.")
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice < 8:
                if choice == 1:
                    add()
                if choice == 2:
                    view()
                if choice == 3:
                    mark()
                if choice == 4:
                    delete()
                if choice == 5:
                    save()
                if choice == 6:
                    load()
                if choice == 7:
                    return
            else:
                print("Enter a valid number under the range.")
        else:
            print("Enter a valid option.")

def add():
    while True:
        task_name = input("Enter your task name (x) to exit: ").capitalize().strip()
        if task_name == "X":
            return
        elif task_name not in tasks:
            description = input("Enter the description about your task: ").capitalize().strip()
            tasks[task_name] = {"Description" : description, "Status" : "Unchecked"}
            print(f"{task_name} has been added in your list.\n")
            return
        else:
            print("Already a same task in your list.\n")

def view():
    if not tasks:
        print("No task added yet!")
        return
    while True:
        task_name = input("Want to see specific task or (Enter) all tasks (x) to exist: ").capitalize().strip()
        if task_name == "X":
            print("Back!\n")
            return
        elif task_name in tasks:
            print(tasks[task_name], "\n")
        elif task_name == "":
            print(tasks, "\n")
        else:
            print("Not in tasks!zn")

def mark():
    if tasks:
        while True:
            task_name = input("Enter task you want to mark (x) to exit: ").capitalize().strip()
            if task_name == "X":
                return
            elif task_name in tasks:
                if tasks[task_name]["Status"] == "Unchecked":
                    tasks[task_name]["Status"] = "Checked"
                    print(f"Task '{task_name}' marked as completed.")
                elif tasks[task_name]["Status"] == "Checked":
                    tasks[task_name]["Status"] = "Unchecked"
                    print(f"Task '{task_name}' marked as unchecked.")
                return
            else:
                if input("Not in your list. View your tasks list (y / n): ").lower() == "y":
                    view()
    else:
        print("No task yet in your list.\n")

def delete():
    if tasks:
        while True:
            delete_option = input("Type 'd' to delete a task and 'c' to clear the entire list (x) to exit: ").strip().lower()
            if delete_option == "x":
                return
            elif delete_option == "d":
                task_name = input("Enter you task name do you want to remove: ").capitalize().strip()
                if task_name in tasks:
                    del tasks[task_name]
                    print(f"{task_name} removed from your list.\n")
                    return
                else:
                    if input("Not in task list! (y) to check you task list (Enter) to skip: ").lower() == "y":
                        view()
            elif delete_option == "c":
                tasks.clear()
                print("All your list have been removed.\n")
                return
            else:
                print("Not an option.\n")
    else:
        print("Your task list is empty!\n")
        return
    
def save():
    if filenames:
        with open(filenames[0], "w") as file:
            json.dump(tasks, file)
    else:
        filename = input("Enter your file name: ").strip() + ".json"
        with open(filename, "w") as file:
            json.dump(tasks, file)
    print("Task have been saved.\n")

def load():
    global tasks, filenames
    while True:
        filename = input("Enter your file name (x) to exit: ").strip() + ".json"
        if filename == "x.json":
            return
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
                filenames = [filename]
            print("Tasks have been loaded.\n")
            return
        except FileNotFoundError:
            print("No saved tasks found.\n")
option()