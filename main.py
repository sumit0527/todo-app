import streamlit as st
from functions import get_todos, write_todos, FILE

st.title("📝 Todo App")
st.subheader("This app will increase your productivity!")


def fetch_todos():
    todos = get_todos(FILE)

    for todo in todos:
        if st.checkbox(todo):
            todos.remove(todo)
            write_todos(todos)
            st.rerun()

def add_todo():
    todos = get_todos()
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    write_todos(todos)

fetch_todos()

st.text_input(label="Enter Todo:",
              placeholder="Enter new todo here...",
              key='new_todo', on_change=add_todo)
