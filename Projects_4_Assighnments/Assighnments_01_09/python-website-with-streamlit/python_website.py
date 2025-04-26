import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student data Generator", layout="wide")
st.title("Student CSV file generator")

names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"]

students = []
for i in range(1, 16):
    student= {
        "ID" : i,
        "Name" : random.choice(names),
        "Age" : random.randint(18,25),
        "Grade" : random.choice(["A", "B", "C", "D", "E"]),
        "Marks" : random.randint(40, 100)
    }
    students.append(student)
    
df = pd.DataFrame(students)
st.subheader("Student data")
st.dataframe(df)


csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV file", csv_file, "students.csv", "text/csv")
st.success("Students Record Generated Successfully!")



