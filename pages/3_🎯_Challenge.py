import streamlit as st

st.set_page_config(page_title="챌린지 목표", page_icon="🎯")

st.title("🎯 습관 형성 프로젝트")
st.write("오늘 달성한 목표를 체크하면 게이지가 올라갑니다.")
st.write("---")

# 미션 리스트 정의
missions = [
    "💧 물 1.5L 이상 마시기",
    "🏃 30분 이상 가볍게 산책 및 운동",
    "📚 책 또는 전공 글 10페이지 이상 읽기",
    "💻 알고리즘 문제 해결 또는 코딩 공부",
    "🧘 명상 및 스트레칭으로 하루 마무리"
]

st.subheader("✅ 오늘의 미션 체크리스트")

# 체크박스를 통해 완료된 미션 개수 계산
completed_count = 0
for mission in missions:
    if st.checkbox(mission):
        completed_count += 1

st.write("---")

# 진행률 계산 및 바(Bar) 시각화
total_missions = len(missions)
progress_percentage = int((completed_count / total_missions) * 100)

st.subheader("📊 오늘의 달성률")
st.progress(completed_count / total_missions)
st.write(f"총 **{total_missions}개** 중 **{completed_count}개** 완료! ({progress_percentage}%)")

# 달성도에 따른 격려 메시지
if progress_percentage == 100:
    st.balloons()
    st.success("🥇 와우! 오늘의 모든 미션을 완벽하게 클리어하셨습니다!")
elif progress_percentage >= 50:
    st.info("👍 절반 이상 성공했네요! 아주 멋진 하루를 보내고 계십니다.")
elif progress_percentage > 0:
    st.warning("🌱 시작이 반입니다! 남은 미션도 천천히 달성해봐요.")
else:
    st.error("💤 아직 완료된 미션이 없습니다. 지금 바로 작은 것부터 시작해볼까요?")
