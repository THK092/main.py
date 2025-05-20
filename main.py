import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 성격/직업/연애 궁합 분석기",
    page_icon="🧠",
    layout="centered"
)

# MBTI 데이터베이스
mbti_data = {
    "INFP": {
        "desc": "🌈 이상주의자이며 내면의 가치와 의미를 중시하는 조용한 중재자입니다.",
        "romance": "💞 깊고 진실된 관계를 선호하며, 감정이 통하는 사람에게 빠르게 빠집니다.",
        "jobs": ["✍️ 작가", "🎨 예술가", "🧘‍♂️ 심리상담사", "🌿 환경운동가"],
        "celebs": ["🎤 BTS의 정국", "🎬 조니 뎁", "📚 셰익스피어"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png"
    },
    "ENTJ": {
        "desc": "🧠 리더형. 계획적이고 논리적이며 리더십이 뛰어난 유형입니다.",
        "romance": "💞 연애에서도 목표지향적이며, 강한 파트너를 찾는 경향이 있습니다.",
        "jobs": ["🏢 CEO", "📈 전략 컨설턴트", "⚖️ 변호사", "🧠 투자 분석가"],
        "celebs": ["🕴 스티브 잡스", "📖 마가렛 대처", "🎬 고든 램지"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333620.png"
    },
    "INFJ": {
        "desc": "🌱 선의의 옹호자. 깊은 통찰력과 공감 능력을 가진 이상주의자입니다.",
        "romance": "💞 감정적으로 깊은 연결을 원하며, 진정한 이해를 추구합니다.",
        "jobs": ["🧘 상담가", "📖 작가", "🧑‍🏫 교사", "⚖️ 인권 변호사"],
        "celebs": ["🎤 테일러 스위프트", "📚 톨스토이", "🧑‍💼 칼 융"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333603.png"
    },
    "ENFP": {
        "desc": "🎉 열정적이고 창의적인 사교가. 자유롭고 다정한 낙천주의자입니다.",
        "romance": "💞 사랑에 있어 모험을 즐기며 감정의 폭이 큽니다.",
        "jobs": ["🎤 방송인", "🎨 디자이너", "📣 마케터", "📸 크리에이터"],
        "celebs": ["🎬 로빈 윌리엄스", "🎤 BTS의 호석", "📚 마크 트웨인"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333610.png"
    }
}

# 웹앱 제목
st.title("💖 MBTI 성격 & 궁합 & 직업 분석기")
st.markdown("당신의 MBTI를 입력하면 분석 결과를 🎆 멋지게 보여드릴게요!")

# 입력받기
user_mbti = st.text_input("🔍 MBTI를 입력하세요 (예: INFP, ENTJ 등):", max_chars=4).upper()

# 분석 출력
if user_mbti:
    if user_mbti in mbti_data:
        info = mbti_data[user_mbti]

        # 이미지 출력
        st.image(info["img"], width=120, caption=f"{user_mbti} 유형")

        # 효과
        st.toast(f"{user_mbti} 분석 완료!", icon="🎇")
        st.balloons()

        # 성격
        st.subheader("👤 성격 설명")
        st.info(info["desc"])

        # 연애 성향
        st.subheader("💞 연애 가치관")
        st.success(info["romance"])

        # 직업 추천
        st.subheader("💼 어울리는 직업")
        for job in info["jobs"]:
            st.markdown(f"- {job}")

        # 유명인사
        st.subheader("🌟 유명인")
        for celeb in info["celebs"]:
            st.markdown(f"- {celeb}")

        # 마무리
        st.markdown("✨ 당신의 성향을 더 깊이 이해하는 데 도움이 되었길 바랍니다!")

    else:
        st.error("❌ 알 수 없는 MBTI입니다. 예: INFP, ENTJ, INFJ, ENFP 등")
        st.snow()

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ by ChatGPT | Powered by Streamlit 🚀")
