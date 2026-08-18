import json
import os

TASKS_FILE = "tasks.txt"

def save_tasks(tasks):
    """Save tasks to file using JSON format"""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
        return True
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")
        return False

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                tasks = json.load(file)
                return tasks if isinstance(tasks, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is corrupted or empty, return empty list
            return []
    return []
