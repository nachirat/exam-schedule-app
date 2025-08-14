
import streamlit as st
import pandas as pd

# Load the cleaned exam schedule data
df = pd.read_csv("cleaned_exam_schedule.csv")

# Configure the Streamlit page
st.set_page_config(page_title="ค้นหาตารางสอบ", layout="wide")
st.title("📘 ค้นหาตารางสอบกลางภาค")
st.write("กรอกชื่อกลุ่มนักศึกษาเพื่อดูตารางสอบที่เกี่ยวข้อง")

# Input field for student group
group_name = st.text_input("🔍 ชื่อกลุ่มนักศึกษา (เช่น 67141EVE1)")

# Filter and display results
if group_name:
    result = df[df['student_group'].astype(str).str.contains(group_name, case=False, na=False)]
    if not result.empty:
        st.success(f"พบ {len(result)} รายการสำหรับกลุ่ม: {group_name}")
        st.dataframe(result)
    else:
        st.warning("ไม่พบข้อมูลสำหรับกลุ่มนี้")
