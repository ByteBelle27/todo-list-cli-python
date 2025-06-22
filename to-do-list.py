tasks = []

def show_menu():
    print("\n📋 Welcome to the NextGen To-Do List")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    date = input("Enter the due date: ")
    tasks.append({"task": task, "due": date})
    print("✅ Task added successfully!")

def view_tasks():
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\n🗂 Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} (Due: {task['due']})")

def delete_task():
    view_tasks()
    if tasks:
        try:
            choice = int(input("Enter the task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"🗑️ Task '{removed['task']}' deleted successfully!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select an option (1-4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("👋 Thanks for using the NextGen To-Do List!")
                break
            else:
                print("❌ Invalid option. Please choose from 1 to 4.")
        except ValueError:
            print("⚠️ Please enter a number.")

if __name__ == "__main__":
    main()
