import streamlit as st
import joblib

model = joblib.load("iris_model.pkl")

st.title("Iris Flower Prediction")
st.write("Enter the flower measurements below to predict its species.")

sl = st.number_input("Sepal Length", min_value=0.0, value=5.1, step=0.1)
sw = st.number_input("Sepal Width", min_value=0.0, value=3.5, step=0.1)
pl = st.number_input("Petal Length", min_value=0.0, value=1.4, step=0.1)
pw = st.number_input("Petal Width", min_value=0.0, value=0.2, step=0.1)

if st.button("Predict"):
    pred = model.predict([[sl, sw, pl, pw]])
    flowers = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"Predicted flower: {flowers[pred[0]]}")
