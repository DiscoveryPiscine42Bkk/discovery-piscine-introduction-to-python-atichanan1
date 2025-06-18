farm_tasks = []

def show_menu():
    print("\n--- Farm Task Manager ---")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Summarize tasks by category")
    print("5. Exit")

def add_task():
    name = input("Enter task name: ")
    print("Select category:")
    print("1. Watering crops")
    print("2. Spraying pesticides")
    print("3. Harvesting produce")
    print("4. Caring for animals")
    category_input = input("Choose (1-4): ")

    categories = {
        "1": "Watering crops",
        "2": "Spraying pesticides",
        "3": "Harvesting produce",
        "4": "Caring for animals"
    }

    category = categories.get(category_input, "Unknown")
    task = {"name": name, "category": category}
    farm_tasks.append(task)
    print("Task added!")

def show_tasks():
    if not farm_tasks:
        print("No tasks yet.")
    else:
        print("\n--- Task List ---")
        for idx, task in enumerate(farm_tasks, start=1):
            print(f"{idx}. {task['name']} ({task['category']})")
def delete_task():
    show_tasks()
    if farm_tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(farm_tasks):
                removed = farm_tasks.pop(task_num - 1)
                print(f"Removed task: {removed['name']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1

    print("\n--- Task Summary ---")
    for category, count in summary.items():
        print(f"{category}: {count} task(s)")
def delete_task():
    show_tasks()
    if farm_tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(farm_tasks):
                removed = farm_tasks.pop(task_num - 1)
                print(f"Removed task: {removed['name']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1
    
    print("\n--- Task Summary ---")
    for category, count in summary.items():
        print(f"{category}: {count} task(s)")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")