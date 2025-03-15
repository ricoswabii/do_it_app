

tasks = []

def show_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in your to-do list.")

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added to your to-do list.')

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f'Task "{removed_task}" removed from your to-do list.')
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1-4.")

if __name__ == "__main__":
    main()
