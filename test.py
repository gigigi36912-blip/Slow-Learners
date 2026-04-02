import streamlit as st

st.set_page_config(page_title="학습 도우미", page_icon="📚", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #4A90E2;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">📚 쉬운 문장 변환기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">어려운 문장을 쉽게 바꿔드립니다 😊</div>', unsafe_allow_html=True)

text = st.text_area("✏️ 문장을 입력하세요", height=150)

if st.button("✨ 변환하기"):
    if text:
        result = text.replace("합니다", "해요").replace("습니다", "어요")
        st.success(result)
    else:
        st.warning("문장을 입력하세요")