FILE = r"TODO-APP\\todos.txt"


def get_todos(FILE_PATH=FILE):
    """Fetch all todos from todo file"""
    with open(FILE, "r") as f:
        content = f.readlines()
    return content


def write_todos(todos, FILE_PATH=FILE):
    """write todos to todos.txt file"""
    with open(FILE_PATH, "w") as f:
        f.writelines(todos)


x = get_todos()
x.append("learning git")
write_todos(x)

print(x)
