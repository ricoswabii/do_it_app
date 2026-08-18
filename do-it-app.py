import os
from data.task_storage import save_tasks, load_tasks
from utils.task_helpers import validate_task, format_task_list, search_tasks

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from storage"""
        self.tasks = load_tasks()
        if not self.tasks:
            print("📂 No existing tasks found. Starting fresh!")
    
    def save_tasks(self):
        """Save tasks to storage"""
        save_tasks(self.tasks)
    
    def show_tasks(self, filtered_tasks=None):
        """Display tasks with formatting"""
        tasks_to_show = filtered_tasks if filtered_tasks is not None else self.tasks
        
        if tasks_to_show:
            print("\n📋 Your To-Do List:")
            print(format_task_list(tasks_to_show))
        else:
            print("\n✨ No tasks in your to-do list. Time to add some!")
    
    def add_task(self, task):
        """Add a new task with validation"""
        if validate_task(task):
            self.tasks.append(task)
            self.save_tasks()
            print(f'✅ Task "{task}" added to your to-do list.')
            return True
        else:
            print("❌ Invalid task. Task cannot be empty or too long.")
            return False
    
    def remove_task(self, task_index):
        """Remove a task by index"""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f'🗑️  Task "{removed_task}" removed from your to-do list.')
            return True
        else:
            print("❌ Invalid task index.")
            return False
    
    def complete_task(self, task_index):
        """Mark a task as complete (adds [COMPLETED] prefix)"""
        if 0 <= task_index < len(self.tasks):
            if not self.tasks[task_index].startswith("[COMPLETED]"):
                self.tasks[task_index] = f"[COMPLETED] {self.tasks[task_index]}"
                self.save_tasks()
                print(f'🎉 Task marked as completed!')
                return True
            else:
                print("⚠️ This task is already completed.")
                return False
        else:
            print("❌ Invalid task index.")
            return False
    
    def search_tasks(self, keyword):
        """Search for tasks containing a keyword"""
        results = search_tasks(self.tasks, keyword)
        if results:
            print(f"\n🔍 Found {len(results)} task(s) containing '{keyword}':")
            self.show_tasks(results)
        else:
            print(f"🔍 No tasks found containing '{keyword}'.")
    
    def clear_all_tasks(self):
        """Clear all tasks with confirmation"""
        if self.tasks:
            confirm = input("⚠️ Are you sure you want to delete ALL tasks? (y/n): ")
            if confirm.lower() == 'y':
                self.tasks = []
                self.save_tasks()
                print("🗑️ All tasks have been cleared.")
                return True
            else:
                print("Operation cancelled.")
                return False
        else:
            print("📭 No tasks to clear.")
            return False

def main():
    manager = TaskManager()
    
    while True:
        print("\n" + "="*40)
        print("📝 TO-DO LIST APPLICATION")
        print("="*40)
        print("1. 📋 Show all tasks")
        print("2. ➕ Add a task")
        print("3. 🗑️ Remove a task")
        print("4. ✅ Complete a task")
        print("5. 🔍 Search tasks")
        print("6. 🧹 Clear all tasks")
        print("7. 📊 Task statistics")
        print("8. 🚪 Exit")
        print("="*40)
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == "1":
            manager.show_tasks()
        
        elif choice == "2":
            task = input("Enter the task you want to add: ").strip()
            manager.add_task(task)
        
        elif choice == "3":
            if manager.tasks:
                manager.show_tasks()
                try:
                    task_index = int(input("Enter the task number to remove: ")) - 1
                    manager.remove_task(task_index)
                except ValueError:
                    print("❌ Invalid input. Please enter a number.")
            else:
                print("📭 No tasks to remove.")
        
        elif choice == "4":
            if manager.tasks:
                manager.show_tasks()
                try:
                    task_index = int(input("Enter the task number to complete: ")) - 1
                    manager.complete_task(task_index)
                except ValueError:
                    print("❌ Invalid input. Please enter a number.")
            else:
                print("📭 No tasks to complete.")
        
        elif choice == "5":
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                manager.search_tasks(keyword)
            else:
                print("❌ Please enter a search keyword.")
        
        elif choice == "6":
            manager.clear_all_tasks()
        
        elif choice == "7":
            total = len(manager.tasks)
            completed = sum(1 for task in manager.tasks if task.startswith("[COMPLETED]"))
            pending = total - completed
            print(f"\n📊 Task Statistics:")
            print(f"   Total tasks: {total}")
            print(f"   ✅ Completed: {completed}")
            print(f"   ⏳ Pending: {pending}")
            if total > 0:
                print(f"   📈 Completion rate: {completed/total*100:.1f}%")
        
        elif choice == "8":
            print("\n👋 Goodbye! Your tasks have been saved.")
            break
        
        else:
            print("❌ Invalid choice. Please select between 1-8.")

if __name__ == "__main__":
  
    os.makedirs("data", exist_ok=True)
    os.makedirs("utils", exist_ok=True)
    

    init_files = ["data/__init__.py", "utils/__init__.py"]
    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write("# Package initialization\n")
    
    main()
