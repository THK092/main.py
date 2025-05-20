import streamlit as st

# 🎨 페이지 꾸미기
st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="💼", layout="centered")

# 🎉 제목 및 설명
st.title("💼 MBTI 기반 직업 추천기")
st.markdown("당신의 MBTI를 입력하면 ✨ 어울리는 직업 ✨을 추천해드릴게요!")
st.markdown("예: `INFP`, `ESTJ`, `ENFP` 등")

# 📊 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "🧮 시스템 분석가", "⚙️ 엔지니어"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "🧪 이론 물리학자", "📝 기술 작가"],
    "ENTJ": ["🚀 기업가", "📈 경영 컨설턴트", "📅 프로젝트 매니저", "👑 CEO"],
    "ENTP": ["🎯 마케팅 전문가", "🧩 기획자", "🌱 스타트업 창업자", "📣 광고 크리에이터"],
    "INFJ": ["🧘 상담가", "🧑‍⚕️ 심리학자", "📖 작가", "⚖️ 인권 운동가"],
    "INFP": ["🎨 예술가", "✍️ 작가", "🧵 디자이너", "🤝 사회복지사"],
    "ENFJ": ["👩‍🏫 교사", "🌍 사회 운동가", "📢 홍보 전문가", "🧑‍💼 조직 관리자"],
    "ENFP": ["🎙️ 방송인", "📹 크리에이터", "🧳 여행 가이드", "🎭 디자이너"],
    "ISTJ": ["📚 회계사", "⚖️ 변호사", "🏛️ 공무원", "💹 재무 분석가"],
    "ISFJ": ["🩺 간호사", "👨‍🏫 교사", "👩‍⚖️ 사회복지사", "📚 사서"],
    "ESTJ": ["🏢 경영자", "🗂️ 프로젝트 매니저", "🪖 군인", "🛠️ 관리자"],
    "ESFJ": ["📞 고객 서비스", "🧑‍⚕️ 간호사", "👩‍🏫 교사", "💼 HR 관리자"],
    "ISTP": ["🔧 기술자", "🧰 정비사", "✈️ 파일럿", "🔍 수사관"],
    "ISFP": ["👨‍🍳 요리사", "👗 패션 디자이너", "📸 사진작가", "🎼 음악가"],
    "ESTP": ["💼 세일즈맨", "🚀 기업가", "🎉 이벤트 플래너", "🏋️ 스포츠 선수"],
    "ESFP": ["🎤 연예인", "🎭 퍼포머", "📣 홍보 전문가", "🎈 이벤트 코디네이터"],
}

# 📥 사용자 입력
user_mbti = st.text_input("🔎 MBTI를 입력하세요 (예: INFP, ESTJ)", max_chars=4).upper()

# 🎁 결과 출력
if user_mbti:
    if user_mbti in mbti_jobs:
        st.success(f"✨ {user_mbti} 유형에게 추천하는 직업은 다음과 같아요!")
        st.markdown("### 📌 추천 직업:")
        for job in mbti_jobs[user_mbti]:
            st.markdown(f"- {job}")

        # 🎈 풍선 효과
        st.balloons()

        # 🧠 추가 메시지
        st.markdown("🌟 당신의 성격에 딱 맞는 길을 걸어보세요! 화이팅 💪")
    else:
        st.error("🚫 올바른 MBTI 유형을 입력해주세요 (예: INFP, ESTJ 등)")
        st.snow()  # ⛄️ 재미 요소로 눈 효과

# 🧡 하단 메시지
st.markdown("---")
st.markdown("Made with ❤️ by ChatGPT | Powered by Streamlit 🚀")
