import streamlit as st
import pandas as pd
      
st.title("Data Dashboard ")
file = st.file_uploader("Choose a csv file", type="csv")

if(file is not None):
    df = pd.read_csv(file)
    st.subheader("Data :")
    st.table(df)
    st.header("Data summary :")
    st.write(df.describe())
    st.subheader("Filter data :")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column " , columns)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_value)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data ")
    x_column = st.selectbox("Select x-axis column", columns, key=1)
    y_column = st.selectbox("Select x-axis column", columns, key=2)
    
    if st.button("Generate table "):
        print(x_column)
        print(y_column)
        st.line_chart(df,x="Date", y="Wind Speed")
        
else :
    st.write("No file uploaded ")