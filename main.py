import streamlit as st
import os
from functions import get_todos, write_todos

FILEPATH = os.path.join("data", "todos.txt")

# app launch startup animation
st.balloons()

st.title("📝 Todo App")
st.subheader("This app will increase your productivity!")

# adding welcome notification 
st.toast("Welcome to our Todo App 😊")


def fetch_todos():
    todos = get_todos()

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


def clear_todos():
    todos = get_todos()
    todos.clear()
    write_todos(todos)


fetch_todos()

# clear all existing todos
st.sidebar.markdown("#### Click below to remove all todos:")
if st.sidebar.button(label="Clear Todos", on_click=clear_todos):
    st.sidebar.success("Todos removed successfully!")

st.text_input(label="Enter Todo:", placeholder="Enter new todo here...", key="new_todo")

st.button(label="Add todo", on_click=add_todo, key="add-todo-btn")
