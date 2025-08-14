
import streamlit as st
import pandas as pd

# Load the cleaned exam schedule data
df = pd.read_csv("cleaned_exam_schedule.csv")

# Configure Streamlit page
st.set_page_config(page_title="ค้นหาตารางสอบ", layout="wide")
st.title("📘 ค้นหาตารางสอบกลางภาค")
st.write("กรอกชื่อกลุ่มนักศึกษา หรือชื่อผู้คุมสอบ หรือชื่อผู้ช่วยคุมสอบ เพื่อดูตารางสอบที่เกี่ยวข้อง")

# Input field for search
query = st.text_input("🔍 คำค้นหา (เช่น 67141EVE1 หรือ นชิรัตน์)")

# Perform search if query is provided
if query:
    # Search in student_group, exam_supervisor, and exam_assistant columns
    result = df[
        df['student_group'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_supervisor'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_assistant'].astype(str).str.contains(query, case=False, na=False)
    ]
    
    if not result.empty:
        st.success(f"พบ {len(result)} รายการที่เกี่ยวข้องกับ: {query}")
        st.dataframe(result)
    else:
        st.warning("ไม่พบข้อมูลที่ตรงกับคำค้นหานี้")
