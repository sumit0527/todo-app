FILE = r'TODO-APP\\todos.txt'

def get_todos(FILE_PATH=FILE):
    ''' Fetch all todos from todo file '''
    with open(FILE, 'r') as f:
        content = f.readlines()
    return content

