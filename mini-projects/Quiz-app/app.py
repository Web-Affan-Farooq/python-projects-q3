# Note . There is an error with the session state and rendering in this app
import streamlit as st 
import json
import random
import matplotlib.pyplot as plt
from typing import Dict,List

# ____Load quesions from json file 
def load_questions():
    with open("./data/questions.json", "r") as f:
        questions = json.load(f)
        return questions
questions = load_questions()[0:11] # Select first 10 questions 

# __Basic structure 
#   {
#     "question": "Which of the following functions converts a string to an integer in Python?",
#     "options": ["str()", "int()", "float()", "chr()"],
#     "correct_answer": "int()"
#   },

# ____Sessionn state working correctly
if("count" not in st.session_state and 
   "quiz_status" not in st.session_state and 
   "selected_options" not in st.session_state and
   "correct_options" not in st.session_state and 
   "score" not in st.session_state):
    
    st.session_state.count = 0  
    st.session_state.selected_options = [] 
    st.session_state.correct_options = []
    st.session_state.score = 0
    st.session_state.quiz_status = False
    
lst = [i for i in range(0,10000)]

def quiz_start():
    for idx,question in enumerate(questions):
        st.write(f"{idx+1}. "+question["question"]) # Write question on screen
        options = question["options"]
        selectd_option_1 = st.checkbox(options[0],key=random.choice(lst))
        selectd_option_2 = st.checkbox(options[1],key=random.choice(lst))
        selectd_option_3 = st.checkbox(options[2],key=random.choice(lst))
        selectd_option_4 = st.checkbox(options[3],key=random.choice(lst))
        st.write("Corrected option : ", question["correct_answer"])
        if(selectd_option_1 == question["correct_answer"]):
            st.session_state.score +=1
            st.write("Score : ", st.session_state.score)
        else :
            pass
        # if selected_option is not None:
        #     # st.write("Selected option ",selected_option)
        #     st.session_state.selected_options.append(selected_option)
        #     # st.write("All selected options :",st.session_state.selected_options)
        #     st.session_state.correct_options.append(question["correct_answer"])
        #     st.session_state.count += 1
        #     st.write(" ")
        #     st.write(" ")
        #     st.write(" ")
        
st.title("Quiz application ")
st.subheader("Let's check how sharp is your python programming skills are ")
if st.button("Start quiz "):
    st.session_state.quiz_status = not st.session_state.quiz_status
    st.write("Session state : ", st.session_state)
    quiz_start()

#     if st.button("Submit"):
#         if(None not in st.session_state.selected_options):
#             st.write("Selected options :",st.session_state.selected_options)
#             st.write("Correct answers : ",st.session_state.correct_options)
#             for i in range(11):
#                 if (st.session_state.selected_options[i] == st.session_state.correct_options[i]): 
#                     score += 1
#                 else : 
#                     pass
#             st.subheader(f"Score : {len(st.session_state.correct_options)-1} / {st.session_state.score}")
    
#             incorrect_answers_count = len(st.session_state.correct_options) - st.session_state.score
#             labels = ['Correct Answers', 'Incorrect Answers']
#             scores = [st.session_state.score, incorrect_answers_count]
#             fig, ax= plt.subplots()
#             ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#1364e8', '#ff6666'], textprops={"color":"white"})    
    
#             ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle
    
#             fig.patch.set_facecolor("#000000")
# # Display the pie chart in Streamlit
#             st.pyplot(fig)
#         else : 
#             st.toast("Please attemp all questions ")
