import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

#Text input
name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")

#Slider to select value
age = st.slider("select your age",0,100)

if age:
    st.write(f"{name}'s age is {age}")


#Drop down menu to select options
options = ['python','java','javascript','go']

choice = st.selectbox("Choose your programming language: ",options)

st.write(f"Your programming language is {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

file = st.file_uploader("Chooe a CSV file",type = "csv")

if file is not None:
    df = pd.read_csv(file)
    st.write(df)