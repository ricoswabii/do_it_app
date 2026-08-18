def validate_task(task):
    """Validate a task before adding"""
    if not task or not task.strip():
        return False
    if len(task) > 200:
        return False
    return True

def format_task_list(tasks):
    """Format tasks for display with numbers and icons"""
    formatted = ""
    for index, task in enumerate(tasks, start=1):
        # Add completion icon
        if task.startswith("[COMPLETED]"):
            icon = "✅"
            task_display = task.replace("[COMPLETED] ", "")
        else:
            icon = "⏳"
            task_display = task
        
        formatted += f"  {index}. {icon} {task_display}\n"
    
    return formatted

def search_tasks(tasks, keyword):
    """Search for tasks containing a keyword (case-insensitive)"""
    keyword = keyword.lower()
    return [task for task in tasks if keyword in task.lower()]

def sort_tasks(tasks, by="priority"):
    """Sort tasks (placeholder for future feature)"""
    # This can be extended for task prioritization
    return tasks
