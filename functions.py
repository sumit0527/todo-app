import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(SCRIPT_DIR, "todos.txt")


def get_todos(FILE):
    """Fetch all todos from todo file"""
    with open(FILE, "r") as f:
        content = f.readlines()
    return content


def write_todos(todos, FILE_PATH=FILEPATH):
    """write todos to todos.txt file"""
    with open(FILE_PATH, "w") as f:
        f.writelines(todos)
