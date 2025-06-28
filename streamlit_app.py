
import streamlit as st

st.set_page_config(page_title="스마트 축구 예측기", layout="wide")

st.title("⚽ 스마트 축구 예측기")
st.markdown("AI 예측 · Sharp 감지 · 배당 흐름 · 대중픽 · 동기부여 · 최근폼 분석")

# 경기 정보
st.subheader("📅 경기 정보")
col1, col2, col3 = st.columns(3)
col1.metric("리그", "EPL")
col2.metric("경기일", "2025-06-29")
col3.metric("경기", "Man City vs Liverpool")

# AI 예측 결과
st.subheader("🧠 AI 예측")
st.info("승 64% / 무 18% / 패 18%")
st.success("Over 65% / Under 35%")

# Sharp 감지
st.subheader("🔥 Sharp 감지")
st.warning("역배당 하락 + 고수 픽 집중")

# 배당 흐름
st.subheader("📈 배당 흐름 (초반 vs 현재)")
st.text("초반: 승 1.85 / 무 3.60 / 패 3.90")
st.text("현재: 승 1.75 / 무 3.80 / 패 4.10")

# 대중픽
st.subheader("📊 대중픽")
st.text("승 68% / 무 15% / 패 17%")

# 최근 폼
st.subheader("⚽ 최근 폼")
st.text("Man City: 승승패무승")
st.text("Liverpool: 승무승승패")

# 동기부여
st.subheader("🏁 동기부여")
st.text("리그 우승 경쟁 중")

st.markdown("---")
st.caption("© 스마트 축구 예측기 · Powered by ChatGPT")
