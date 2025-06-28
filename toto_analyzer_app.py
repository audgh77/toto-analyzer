
import streamlit as st

st.set_page_config(page_title="토토 분석기", layout="wide")

st.title("⚽ 토토 분석기")
st.markdown("이 앱은 축구 경기 예측을 위한 분석 도구입니다.")

with st.expander("📊 최근 경기 분석"):
    st.write("여기에 최근 경기 5개 자동 분석 내용이 들어갑니다.")

with st.expander("🚑 주전 선수 부상자"):
    st.write("여기에 부상자 정보가 들어갑니다.")

with st.expander("🔍 AI 예측 / 샤프 감지 / 배당 흐름"):
    st.write("여기에 AI 기반 예측, 샤프 감지, 배당 흐름 정보가 들어갑니다.")

st.success("아래로 내려가서 추가 분석 결과를 확인하세요.")
