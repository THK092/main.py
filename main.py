import streamlit as st
from PIL import Image

# 🎯 페이지 설정
st.set_page_config(
    page_title="MBTI 성격 & 직업 추천기 🎆",
    page_icon="🧠",
    layout="centered",
)

# 🔥 상단 타이틀 및 설명
st.title("🎆 MBTI 성격 & 직업 추천기 🎇")
st.markdown("당신의 MBTI를 입력하면 ✨ **성격 특성**과 어울리는 **추천 직업** ✨을 알려드릴게요!")
st.markdown("예: `INFP`, `ESTJ`, `ENFP` ...")

# 🔍 사용자 입력
user_mbti = st.text_input("📩 MBTI를 입력하세요:", max_chars=4).upper()

# 🧩 MBTI 데이터베이스
mbti_info = {
    "INFP": {
        "desc": "🌈 이상주의자이며 조용하고 따뜻한 성격의 소유자. 내면의 가치와 의미를 중요시합니다.",
        "jobs": ["🎨 예술가", "📖 작가", "🧘 상담가", "🌍 사회복지사"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png",
    },
    "ESTJ": {
        "desc": "📊 논리적이고 체계적이며 현실적인 리더. 책임감이 강하고 조직을 잘 이끕니다.",
        "jobs": ["🏛️ 관리자", "💼 경영자", "🪖 군인", "📋 프로젝트 매니저"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333600.png",
    },
    "ENFP": {
        "desc": "🎉 자유로운 영혼의 사교가. 창의적이고 열정적이며 타인에게 영감을 줍니다.",
        "jobs": ["🎤 방송인", "🧳 여행가이드", "📹 콘텐츠 크리에이터", "🎭 디자이너"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333610.png",
    },
    "INTJ": {
        "desc": "🧠 전략가. 독립적이고 분석적인 성격으로 장기적인 계획에 강합니다.",
        "jobs": ["📈 전략 컨설턴트", "🧮 데이터 분석가", "🧪 연구자", "⚙️ 엔지니어"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333620.png",
    }
}

# 🚀 결과 출력
if user_mbti:
    if user_mbti in mbti_info:
        data = mbti_info[user_mbti]

        # 🎇 폭죽 효과
        st.toast(f"{user_mbti} 유형 분석 완료!", icon="🎆")
        st.balloons()

        # 🖼️ 이미지 표시
        st.image(data["img"], width=120, caption=f"{user_mbti} 유형")

        # 💬 성격 설명
        st.markdown(f"### 👤 {user_mbti}의 성격")
        st.info(data["desc"])

        # 💼 추천 직업
        st.markdown("### 💼 어울리는 직업")
        for job in data["jobs"]:
            st.success(f"- {job}")

        # 🎉 응원 메시지
        st.markdown("🌟 당신의 성격에 딱 맞는 길을 응원합니다! 화이팅! 💪")

    else:
        st.error("🚫 등록되지 않은 MBTI 유형입니다. 예: INFP, ESTJ, ENFP, INTJ 등")
        st.snow()

# 📌 푸터
st.markdown("---")
st.markdown("Made with ❤️ by ChatGPT | Powered by Streamlit 🚀")
