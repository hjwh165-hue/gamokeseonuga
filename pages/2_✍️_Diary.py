import streamlit as st
import datetime

st.set_page_config(page_title="감정 일기장", page_icon="✍️")

st.title("✍️ 한 줄 감정 일기장")
st.write("오늘 하루는 어땠나요? 소중한 일상을 기록해 보세요.")
st.write("---")

# 입력을 받기 위한 폼(Form) 구성
with st.form("diary_form"):
    today = st.date_input("날짜 선택", datetime.date.today())
    mood = st.select_slider(
        "오늘의 기분 점수",
        options=["😢 피곤해요", "😐 그저 그래요", "🙂 괜찮아요", "🥰 최고예요!"]
    )
    title = st.text_input("일기 제목")
    content = st.text_area("오늘 있었던 일을 적어주세요")
    
    submit_button = st.form_submit_button("일기 저장하기")

# 저장 버튼을 눌렀을 때 반응
if submit_button:
    if title and content:
        st.success("🎉 일기가 성공적으로 등록되었습니다!")
        st.write("---")
        st.markdown(f"### 🗓️ {today} | 기분: {mood}")
        st.markdown(f"**제목: {title}**")
        st.info(content)
    else:
        st.warning("제목과 내용이 모두 입력되어야 저장할 수 있습니다.")
