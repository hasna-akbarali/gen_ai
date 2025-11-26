import streamlit as st
import pandas as pd

st.title('Basics of Python')

name = st.text_input('What is your name?')
age = st.slider('How old are you?', 0, 100)

if name:
    st.write(f'Hello, {name}!', f'You are {age} years old.')

options = ['Cats', 'Dogs', 'Birds']
selected = st.selectbox('What is your favorite animal?', options)

if selected:
    st.write(f'You selected {selected}')

df = pd.DataFrame({'1':{'Employee_Name':'John', 'Salary':1000, 'Age':30}, 
                   '2':{'Employee_Name':'Mary', 'Salary':2000, 'Age':25}, 
                   '3':{'Employee_Name':'Tom', 'Salary':1500, 'Age':35}})

df.to_csv('employee_data.csv', index=False)

st.download_button('Download CSV', data=open('employee_data.csv', 'r'), file_name='employee_data.csv')