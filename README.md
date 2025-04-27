# Task Tracker CLI

## Introduction
`task_cli.py` is a simple command-line interface (CLI) application designed to help you track and manage your tasks effectively. It allows you to:
- Add, update, and delete tasks.
- Mark tasks as in progress or done.
- List tasks based on their status.

This project uses a JSON file for persistent storage, ensuring your tasks are saved and retrievable even after the program ends.

---

## Features
- **Add Tasks:** Create new tasks with a description.
- **Update Tasks:** Modify the description of existing tasks.
- **Delete Tasks:** Remove tasks that are no longer needed.
- **Mark Tasks:** Change a task's status to `in-progress` or `done`.
- **List Tasks:** View tasks by status or see all tasks.

---

## Prerequisites
- Python 3.x installed on your system.
- Basic familiarity with running commands in the terminal.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JessieRuben1/task_tracker.git
   cd task_tracker

# Usage
Run the script using Python, followed by the desired command and arguments.

**Adding a Task:**
`bash
python task_cli.py add "Buy groceries"`

**Updating a Task:**
`bash
python task_cli.py update 1 "Buy groceries and cook dinner"`

**Deleting a Task:**
`bash
python task_cli.py delete 1`

**Marking a Task as In Progress or Done:**
`bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1`

## Listing Tasks
`bash
List all tasks
python task_cli.py list`

**List tasks by status:**
`python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress`

# Handling Errors
If you encounter "Task not found," ensure the ID you specified exists.

If the script doesn’t run, confirm Python is correctly installed and added to your system’s PATH.

# Roadmap
Planned features for future updates:
Enhanced task search functionality.
Sorting tasks by creation or update date.
Support for priority levels (e.g., high, medium, low).

# License
This project is licensed under the MIT License.

# Contribution
Feel free to fork the repository and make a pull request for any improvements or additional features you’d like to contribute!

# URL
https://github.com/JessieRuben1/task_tracker/edit/main/README.md

# Author
Developed by Jessie Ruben. 😊
