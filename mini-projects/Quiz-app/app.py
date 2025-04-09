# Note . There is an error with the session state and rendering in this app
import streamlit as st 
import json
import random
import matplotlib.pyplot as plt

def load_questions():
    with open("./data/questions.json", "r") as f:
        questions = json.load(f)
        return questions
    
st.title("Quiz application ")
st.subheader("Let's check how sharp is your python programming skills are ")

questions = load_questions()[0:11]

#   {
#     "question": "Which of the following functions converts a string to an integer in Python?",
#     "options": ["str()", "int()", "float()", "chr()"],
#     "correct_answer": "int()"
#   },

if("count" not in st.session_state):
    st.session_state.count = 0  
if("selected_options" not in st.session_state):
    st.session_state.selected_options = [] 
if("correct_options" not in st.session_state):
    st.session_state.correct_options = []
if("score" not in st.session_state):
    st.session_state.score = 0
    
if st.button("Start quiz "):

    for question in questions:
        st.write(f"{st.session_state.count}. "+question["question"])
        options = question["options"]
        selected_option = st.radio("",options=options,index=None, key=st.session_state.count)
        st.session_state.selected_options.append(selected_option)
        st.session_state.correct_options.append(question["correct_answer"])
        st.session_state.count += 1
        st.write(" ")
        st.write(" ")
        st.write(" ")

    if st.button("Submit"):
        if(None not in st.session_state.selected_options):
            st.write("Selected options :",st.session_state.selected_options)
            st.write("Correct answers : ",st.session_state.correct_options)
            for i in range(11):
                if (st.session_state.selected_options[i] == st.session_state.correct_options[i]): 
                    score += 1
                else : 
                    pass
            st.subheader(f"Score : {len(st.session_state.correct_options)-1} / {st.session_state.score}")
    
            incorrect_answers_count = len(st.session_state.correct_options) - st.session_state.score
            labels = ['Correct Answers', 'Incorrect Answers']
            scores = [st.session_state.score, incorrect_answers_count]
            fig, ax= plt.subplots()
            ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#1364e8', '#ff6666'], textprops={"color":"white"})    
    
            ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle
    
            fig.patch.set_facecolor("#000000")
# Display the pie chart in Streamlit
            st.pyplot(fig)
        else : 
            st.toast("Please attemp all questions ")
