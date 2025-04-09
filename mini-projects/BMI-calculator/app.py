import streamlit as st

def calculate_bmi(weight, height):
    try :
        if(int(height) == 0):
            st.write("Height cannot be zero ")
        else: 
            calc = int(weight) / int(height)**2    
            st.write(f"Calculated BMI is {calc}")
    except ValueError:
        st.toast("Please enter a valid integer ")
  
st.title("BMI Calculator App In Streamlit ")
weight = st.text_input("Enter your weight in kgs ")
height = st.text_input("Enter your height in meters ")

st.button("Calculate BMI ", on_click=calculate_bmi(weight, height))
