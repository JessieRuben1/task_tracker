
import json
import sys
from datetime import datetime

# Define the path to the task file
TASK_FILE = "tasks.json"

# Load tasks from the JSON file, or create the file if it does not exists
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "incomplete",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"New Task has been added successfully (ID: {new_task['id']})")

# update an existing task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            #task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")
    
# delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully")
    
# Mark a task as pending or done
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks()
            print(f"Task marked as {status}")
            return
    print("Task not found")

# list tasks based on their status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, CreatedAt: {task['createdAt']}, UpdatedAt: {task['updatedAt']}")

# MAIN FUNCTION TO HANDLE COMMAND-LINE ARGUEMENTS
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> <args>")
        return
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
            return
        add_task(sys.argv[2])
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> <new_description>")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
            return
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
            return
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
            return
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Error: Unknown command")
        
if __name__ == "__main__":
    main()