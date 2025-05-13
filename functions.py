FILE = r"D:\Python Projects\My Own Projects\TODO-APP\todos.txt"


def get_todos(FILE_PATH=FILE):
    """Fetch all todos from todo file"""
    with open(FILE, "r") as f:
        content = f.readlines()
    return content


def write_todos(todos, FILE_PATH=FILE):
    """write todos to todos.txt file"""
    with open(FILE_PATH, "w") as f:
        f.writelines(todos)
