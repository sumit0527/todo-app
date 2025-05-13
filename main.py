import streamlit as st
from functions import get_todos, write_todos, FILE

st.title("📝 Todo App")
st.subheader("This app will increase your productivity!")

def fetch_todos():
    todos = get_todos(FILE)

    for todo in todos:
        st.checkbox(todo)


if __name__ == "__main__":
    fetch_todos()
