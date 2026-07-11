import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="My Daily Hub",
    page_icon="🏠",
    layout="centered"
)

# 홈 화면 콘텐츠
st.title("🏠 Welcome to My Daily Hub!")
st.subheader("파이썬과 스트림릿으로 만든 나만의 멀티 페이지 앱입니다.")
st.write("---")

st.markdown("""
왼쪽 사이드바를 보시면 자동으로 페이지 메뉴가 생성된 것을 확인할 수 있습니다! 
원하는 페이지를 클릭해 이동해 보세요.

### 🧭 페이지 안내
*   **📊 Page 1. 대시보드 (Dashboard)**: 오늘의 주요 수치와 간단한 데이터 시각화 차트를 확인합니다.
*   **✍️ Page 2. 감정 일기장 (Diary)**: 오늘 하루 있었던 일과 감정을 기록하고 저장합니다.
*   **🎯 Page 3. 챌린지 달성도 (Challenge)**: 나만의 목표를 설정하고 달성도를 실시간으로 체크합니다.
""")

st.info("💡 팁: `pages/` 폴더 안에 새로운 `.py` 파일을 추가하면 사이드바 메뉴가 자동으로 늘어납니다!")

st.write("---")
st.caption("© 2026 My Daily Hub | Powered by Streamlit Multi-page Feature")
