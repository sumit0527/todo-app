import os

FILEPATH = os.path.join("data", "todos.txt")


def get_todos(FILE=FILEPATH):
    """Fetch all todos from todo file"""
    with open(FILE, "r") as f:
        content = f.readlines()
    return content


def write_todos(todos, FILEPATH=FILEPATH):
    """write todos to todos.txt file"""
    with open(FILEPATH, "w") as f:
        f.writelines(todos)
