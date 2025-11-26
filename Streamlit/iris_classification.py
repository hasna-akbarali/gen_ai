import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df,iris.target_names

df,target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df.species)

st.sidebar.title('Iris Classification')

sepal_length = st.sidebar.slider('Sepal Length', min_value=4, max_value=8, value=5)
sepal_width = st.sidebar.slider('Sepal Width', min_value=2, max_value=4, value=3)
petal_length = st.sidebar.slider('Petal Length', min_value=1, max_value=6, value=3)
petal_width = st.sidebar.slider('Petal Width', min_value=0, max_value=2, value=1)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)

st.write(f'Sepal Length: {sepal_length}, Sepal Width: {sepal_width}, Petal Length: {petal_length}, Petal Width: {petal_width}')
st.write(f'Prediction: {target_names[prediction[0]]}')