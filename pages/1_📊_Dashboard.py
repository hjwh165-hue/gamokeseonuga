import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="나의 대시보드", page_icon="📊")

st.title("📊 나의 주간 라이프 통계")
st.write("이번 주 나의 수면 패턴과 공부 집중 시간을 분석합니다.")
st.write("---")

# 가상의 주간 데이터 생성
data = {
    "요일": ["월", "화", "수", "목", "금", "토", "일"],
    "수면시간(시간)": [6.5, 7.0, 5.5, 6.0, 7.5, 8.5, 8.0],
    "집중시간(시간)": [4.0, 5.5, 6.0, 3.5, 4.5, 2.0, 1.5]
}
df = pd.DataFrame(data)

# 대시보드 상단 요약 지표
col1, col2 = st.columns(2)
col1.metric(label="평균 수면 시간", value=f"{df['수면시간(시간)'].mean():.1f} 시간", delta="0.5 시간 증가")
col2.metric(label="총 집중 시간", value=f"{df['집중시간(시간)'].sum()} 시간", delta="-2 시간 감소", delta_color="inverse")

st.write("---")

# Plotly를 이용한 상호작용 차트
st.subheader("📈 요일별 시간 변화 그래프")
chart_target = st.selectbox("확인할 지표를 고르세요:", ["수면시간(시간)", "집중시간(시간)"])

fig = px.line(df, x="요일", y=chart_target, markers=True, 
              title=f"요일별 {chart_target} 추이",
              color_discrete_sequence=["#FF4B4B"])
st.plotly_chart(fig, use_container_width=True)
