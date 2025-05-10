import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="🏋️", layout="centered")
st.title("BMI CALCULATOR")

st.markdown("""     
   This is a simple BMI calculator that allows you to calculate your Body Mass Index (BMI) based on your **height and weight**.
   """)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (in kg ) : ", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Enter your height (in cm) : ", min_value=1.0, format="%.2f")   # format
    
if height > 0 and weight > 0 :
    bmi = weight / height ** 2 
    st.subheader("Your BMI is : ")
    st.markdown(f"{bmi:.2f}", unsafe_allow_html=True) 
    
    if bmi < 18.5:
        st.error("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
else:
    st.info("Please enter a valid weight amnd height.")