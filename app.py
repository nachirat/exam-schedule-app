
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ค้นหาตารางสอบ", layout="wide")
st.title("📘 ค้นหาตารางสอบกลางภาค")
st.write("กรอกคำค้น เช่น ชื่อกลุ่มนักศึกษา หรือชื่อผู้คุมสอบ เพื่อดูตารางสอบที่เกี่ยวข้อง")

df = pd.read_csv("cleaned_exam_schedule.csv")

query = st.text_input("🔍 คำค้น (ชื่อกลุ่มนักศึกษา หรือชื่อผู้คุมสอบ)")

if query:
    result = df[
        df['student_group'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_supervisor'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_assistant'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_supervisor_1'].astype(str).str.contains(query, case=False, na=False) |
        df['exam_assistant_1'].astype(str).str.contains(query, case=False, na=False)
    ]
    if not result.empty:
        st.success(f"พบ {len(result)} รายการที่เกี่ยวข้องกับ: {query}")
        st.dataframe(result)
    else:
        st.warning("ไม่พบข้อมูลที่ตรงกับคำค้นนี้")
