import streamlit as st

st.set_page_config(
    page_title="MBTI 분석 웹앱",
    page_icon="🧠",
    layout="centered"
)

# 16가지 MBTI 데이터
mbti_data = {
    "INTJ": {
        "desc": "🧠 전략가. 분석적이고 독립적인 완벽주의자입니다.",
        "romance": "💞 깊고 진지한 관계를 선호하지만 표현은 서툴 수 있어요.",
        "jobs": ["📈 전략기획가", "💻 개발자", "🧪 연구원", "⚖️ 법률가"],
        "celebs": ["🎬 엘론 머스크", "📖 아놀드 슈워제네거", "🎮 마크 저커버그"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333620.png"
    },
    "INTP": {
        "desc": "🔍 논리적인 사색가. 새로운 아이디어에 집착하는 철학자형입니다.",
        "romance": "💞 감정보다 지적 대화에 끌리며 천천히 다가갑니다.",
        "jobs": ["🧠 학자", "🧪 데이터 과학자", "💻 개발자", "🎓 교수"],
        "celebs": ["📚 알베르트 아인슈타인", "🧙 뉴턴", "📽 에이브러햄 링컨"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333617.png"
    },
    "ENTJ": {
        "desc": "📊 지도자형. 통찰력과 추진력을 가진 타고난 리더입니다.",
        "romance": "💞 목표지향적이며, 강한 관계를 원합니다.",
        "jobs": ["🏛️ CEO", "⚖️ 변호사", "📈 컨설턴트", "🧠 전략가"],
        "celebs": ["🧑‍💼 스티브 잡스", "🏛 마가렛 대처", "🍳 고든 램지"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333620.png"
    },
    "ENTP": {
        "desc": "🌀 토론가형. 창의적이고 호기심 많은 아이디어 뱅크입니다.",
        "romance": "💞 활발하고 자극적인 관계를 즐깁니다.",
        "jobs": ["🎤 방송인", "📣 마케터", "🧠 창업가", "🎭 디자이너"],
        "celebs": ["🎬 로버트 다우니 주니어", "📣 토마스 에디슨", "🎤 톰 행크스"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333618.png"
    },
    "INFJ": {
        "desc": "🌱 통찰력 있는 이상주의자. 조용하지만 영향력 있는 성격입니다.",
        "romance": "💞 깊은 감정적 유대감을 중요시합니다.",
        "jobs": ["📖 작가", "🧘 상담가", "🧑‍🏫 교사", "🎨 인권운동가"],
        "celebs": ["🎤 테일러 스위프트", "📚 칼 융", "🎬 니콜 키드먼"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333603.png"
    },
    "INFP": {
        "desc": "🌈 중재자형. 조용하고 따뜻하며 이상을 좇는 이상주의자입니다.",
        "romance": "💞 진심어린 사랑을 추구하며 섬세한 감정을 가졌습니다.",
        "jobs": ["✍️ 작가", "🧘 상담사", "🎨 예술가", "🌿 사회복지사"],
        "celebs": ["🎤 정국", "🎬 조니 뎁", "📖 셰익스피어"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png"
    },
    "ENFJ": {
        "desc": "🤝 정의로운 사회운동가. 타인을 돕고자 하는 따뜻한 리더입니다.",
        "romance": "💞 헌신적인 연애를 하며 감정적 소통을 중시합니다.",
        "jobs": ["🧑‍🏫 교사", "🧘 심리상담사", "🎤 연설가", "⚖️ NGO활동가"],
        "celebs": ["🎤 오프라 윈프리", "📚 마틴 루터 킹", "🎬 에마 왓슨"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333611.png"
    },
    "ENFP": {
        "desc": "🎉 열정적인 사교가. 창의적이며 감정 표현이 풍부합니다.",
        "romance": "💞 즐겁고 감성적인 연애를 추구합니다.",
        "jobs": ["🎤 연예인", "📣 마케터", "🎨 크리에이터", "🧳 여행가이드"],
        "celebs": ["🎬 로빈 윌리엄스", "🎤 호석", "📚 마크 트웨인"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333610.png"
    },
    "ISTJ": {
        "desc": "📘 책임감 강한 관리자형. 안정과 질서를 추구합니다.",
        "romance": "💞 실용적인 연애를 하며 믿음이 우선입니다.",
        "jobs": ["👮 경찰", "💼 공무원", "📊 회계사", "⚖️ 법률가"],
        "celebs": ["🧑‍💼 나폴레옹", "📚 워렌 버핏", "🎬 맷 데이먼"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333601.png"
    },
    "ISFJ": {
        "desc": "🛡 수호자형. 헌신적이고 배려 깊은 조용한 보호자입니다.",
        "romance": "💞 깊은 감정적 유대와 안정감을 중시합니다.",
        "jobs": ["👩‍⚕️ 간호사", "🏫 교사", "💬 상담가", "👵 복지사"],
        "celebs": ["👩‍🎤 비욘세", "📖 마더 테레사", "🏛 조지 워싱턴"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333602.png"
    },
    "ESTJ": {
        "desc": "📊 경영자형. 현실적이고 체계적인 관리자입니다.",
        "romance": "💞 책임감 있는 사랑을 하며 미래를 설계합니다.",
        "jobs": ["🏛 관리자", "💼 경영인", "⚖️ 판사", "🪖 군인"],
        "celebs": ["🎬 헨리 포드", "📊 마사 스튜어트", "🕴 프랭크 시나트라"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333600.png"
    },
    "ESFJ": {
        "desc": "🌸 친절한 돌봄이. 사교적이고 조화를 중시합니다.",
        "romance": "💞 정서적으로 안정된 관계를 추구합니다.",
        "jobs": ["👩‍🏫 교사", "👩‍⚕️ 간호사", "👨‍🍳 요리사", "🎤 아나운서"],
        "celebs": ["🎤 테일러 스위프트", "🎬 제니퍼 가너", "📺 휴 그랜트"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333604.png"
    },
    "ISTP": {
        "desc": "🛠 장인형. 분석적이며 도구를 잘 다루는 현실주의자입니다.",
        "romance": "💞 연애보다는 자유를 중시하지만 깊은 감정도 내포합니다.",
        "jobs": ["🔧 엔지니어", "🚒 구조대", "🚗 정비사", "🏍 드라이버"],
        "celebs": ["🎮 브루스 윌리스", "🎬 클린트 이스트우드", "📽 해리슨 포드"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333605.png"
    },
    "ISFP": {
        "desc": "🎨 예술가형. 온화하고 감성적이며 미적 감각이 뛰어납니다.",
        "romance": "💞 로맨틱하고 조용한 사랑을 꿈꿉니다.",
        "jobs": ["🎨 화가", "📷 포토그래퍼", "🎭 배우", "🌷 플로리스트"],
        "celebs": ["🎬 마이클 잭슨", "🎤 브리트니 스피어스", "📸 오드리 햅번"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333606.png"
    },
    "ESTP": {
        "desc": "⚡ 활동가형. 에너지 넘치고 현실 감각이 뛰어납니다.",
        "romance": "💞 도전적인 연애를 선호하고 직설적입니다.",
        "jobs": ["🎤 MC", "🚓 경찰", "🕴 세일즈", "🏀 운동선수"],
        "celebs": ["🎬 어니스트 헤밍웨이", "🎮 에디 머피", "🎤 마돈나"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333607.png"
    },
    "ESFP": {
        "desc": "🎊 연예인형. 사교적이고 즐거움을 추구하는 삶의 예술가입니다.",
        "romance": "💞 사랑을 통해 자신을 표현하고 즐깁니다.",
        "jobs": ["🎤 가수", "🎭 배우", "🎧 DJ", "👗 스타일리스트"],
        "celebs": ["🎬 마일리 사이러스", "🎤 아델", "📺 엘튼 존"],
        "img": "https://cdn-icons-png.flaticon.com/512/4333/4333608.png"
    }
}

# 타이틀
st.title("💖 MBTI 성격·연애·직업 분석기")
st.markdown("당신의 MBTI를 입력하세요! 결과와 함께 🎆 효과도 함께 보여드립니다.")

# 입력창
user_mbti = st.text_input("🔤 MBTI를 입력해주세요 (예: INFP, ENTJ 등):", max_chars=4).upper()

# 분석 출력
if user_mbti:
    if user_mbti in mbti_data:
        info = mbti_data[user_mbti]
        st.image(info["img"], width=120, caption=f"{user_mbti} 유형")
        st.toast(f"{user_mbti} 분석 완료!", icon="💡")
        st.balloons()

        st.subheader("🧠 성격")
        st.info(info["desc"])

        st.subheader("💞 연애 가치관")
        st.success(info["romance"])

        st.subheader("💼 추천 직업")
        for job in info["jobs"]:
            st.markdown(f"- {job}")

        st.subheader("🌟 유명인")
        for celeb in info["celebs"]:
            st.markdown(f"- {celeb}")

        st.markdown("---")
        st.markdown("Made with ❤️ by ChatGPT")
    else:
        st.error("❌ 올바르지 않은 MBTI입니다. 16가지 유형 중 하나를 입력해주세요.")
        st.snow()
