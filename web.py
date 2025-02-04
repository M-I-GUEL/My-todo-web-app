import streamlit as sl
from todo_functions import get_todo, write_todo
todos = get_todo()
def add_todo():
   new_todo = sl.session_state['todo']+'\n'
   todos.append(new_todo)
   write_todo(todos)
sl.title('My Todo App')
sl.subheader("let's go boy!")
sl.write('This app is for productivity!')
for index, todo in enumerate(todos):
  check_box = sl.checkbox(todo, key=f'todo:{index}')
  if check_box:
    todos.pop(index)
    write_todo(todos)
    del sl.session_state[f'todo:{index}']
    sl.rerun()
sl.text_input(label='',
placeholder='Add a todo...',key='todo',on_change=add_todo)
