import streamlit as st
from functions import get_todos, write_todos, FILE

st.title("📝 Todo App")
st.subheader("This app will increase your productivity!")


def fetch_todos():
    todos = get_todos(FILE)

    for key, todo in enumerate(todos, start=1):
        if st.checkbox(todo, key=key):
            todos.remove(todo)
            write_todos(todos)
            st.rerun()


def add_todo():
    todos = get_todos()
    todo = st.session_state["new_todo"]
    st.session_state["new_todo"] = ""
    todos.append(todo + "\n")
    write_todos(todos)


fetch_todos()

st.text_input(label="Enter Todo:", placeholder="Enter new todo here...", key="new_todo")

st.button(label="Add todo", on_click=add_todo, key="add-todo-btn")
