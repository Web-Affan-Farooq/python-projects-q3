import streamlit as st
from datetime import date

if("Todos" not in st.session_state 
   and "add_field_status" not in st.session_state
   and "edit_field_status" not in st.session_state):
    st.session_state.Todos = []
    st.session_state.add_field_status = False
    st.session_state.edit_field_status = False
    
# ____For pushing todos in list present in session state
def create_todo(todo):
    st.session_state.Todos.append(todo)
    st.toast("Todo added successfully")
    st.session_state.add_field_status = False # status not toogling 
    st.session_state.edit_field_status = False # status not toogling 
    st.write("Todos pushed : ",todo)
    st.write("Current session state : ", st.session_state)
    
def show_fields():
    title = st.text_input("Enter title")
    description = st.text_area("Enter description")
    due_date = st.date_input("Enter due date")
    if(title != "" and description != ""):
        data = {
            "title":title,
            "description":description,
            "due-date":due_date,
            "done":False,
            "created_at":date.today()
            }
        st.write("Title : ",title)
        st.write("Description : ",description)
        st.write("Duedate : ",due_date)
        if st.button("Create todo"):
                return create_todo(data)
        # print(f"Today is {date.today()}")
        # print("title : ",title)
        # print("description : ",description)
        # print("duedate : ", due_date)

st.title("Todolist application")
create_todo_tab , edit_todo_tab, list_tab = st.tabs(["Create todos", "Edit todos ", "List"])
with create_todo_tab:
    st.session_state.add_field_status = True
    show_fields()
    
with edit_todo_tab:
    options = [todo["title"] for todo in st.session_state.Todos]
    options.insert(0, "No option selected")
    selected_todo_title = st.selectbox(label="Select todo ", options=options)
    selected_todo = {}
    if(selected_todo_title != options[0]):        
        for todo in st.session_state.Todos:
            if(todo["title"] == selected_todo_title):
                selected_todo = todo
            else : pass
        new_title = st.text_input("Todo title ", value=selected_todo["title"])
        new_description = st.text_input("Todo description ", value=selected_todo["description"])
        new_due_date = st.date_input("Todo title ", value=selected_todo["due-date"])
        
        todo_index = options.index(selected_todo_title) - 1 # because we have added a default value "no option sleected in the list "
        
        st.write("index : ", todo_index)
        if st.button("Save"):
            st.session_state.Todos[todo_index]["title"] = new_title 
            st.session_state.Todos[todo_index]["description"] = new_description
            st.session_state.Todos[todo_index]["due-date"] = new_due_date 
            st.toast("Saved ")
            selected_todo_title = "No option selected"
            st.rerun()
    st.write(selected_todo)

with list_tab:
    def mark_as_done(todo_title, status):
        for i, todo in enumerate(st.session_state.Todos):
            if todo["title"] == todo_title:
                st.session_state.Todos[i]["done"] = status
                st.toast("Status updated")
                st.rerun()

    if st.session_state.Todos:
        for todo in st.session_state.Todos:
            st.write("#### Title:", todo["title"])
            st.write("Description:", todo["description"])
            st.write("Due date:", todo["due-date"])
            st.write("Created at:", todo["created_at"])

            if todo["done"]:
                st.success("✅ Completed")
                if st.button("Mark as Remaining", key=f"remaining_button_{todo['title']}"):
                    mark_as_done(todo["title"], False)
            else:
                st.warning("⏳ Remaining")
                if st.button("Mark as Done", key=f"done_button_{todo['title']}"):
                    mark_as_done(todo["title"], True)

            st.divider()
    else:
        st.info("No todos found...")