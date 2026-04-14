import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Hello streamlit")

#Simple text
st.write("This is a simple text")

# create a simple dataframe

df = pd.DataFrame({
    'first_comlumn' : [1,2,3,4,5],
    'second_column':[6,7,8,9,10]
})

# Displaying the dataframe

st.write("Dataframe")
st.write(df)

#Line chart

chart_data = pd.DataFrame(
    np.random.rand(20,3), columns = ['a','b','c']
)

#Display of line chart

st.line_chart(chart_data)