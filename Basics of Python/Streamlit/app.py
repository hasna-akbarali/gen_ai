import streamlit as st 
import pandas as pd
import numpy as np

st.title('Basics of Python')

st.write('Hello, Streamlit!')

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
st.write(df)

# create a line chart
st.line_chart(df)

# create a bar chart
st.bar_chart(df)

# create a table
st.table(df)

# create a slider
slider = st.slider('Number of bars')

# create a checkbox
checkbox = st.checkbox('Show a bar chart')

if checkbox:
    # create a bar chart
    st.bar_chart(df)