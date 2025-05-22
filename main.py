# mbti_app.py

import streamlit as st
import time

# 16가지 MBTI 정보
mbti_descriptions = {
    "INTJ": {
        "title": "전략가 (INTJ)",
        "personality": "독립적이고 분석적인 사고를 중시하며, 체계적이고 계획적인 성향입니다.",
        "love": "연애에서 감정보다 논리적 호환성과 장기적 가능성을 따집니다. 진지하고 헌신적인 편입니다.",
    },
    "INTP": {
        "title": "논리술사 (INTP)",
        "personality": "호기심 많고 분석적이며, 복잡한 문제를 깊이 있게 탐구하는 것을 좋아합니다.",
        "love": "연애에 있어서도 독립성과 지적 자극을 중요하게 생각합니다.",
    },
    "ENTJ": {
        "title": "통솔자 (ENTJ)",
        "personality": "리더십이 뛰어나며, 목표 달성을 위해 논리적으로 계획하고 추진합니다.",
        "love": "연애에서도 리더십이 강하며, 진취적이고 확신에 찬 관계를 선호합니다.",
    },
    "ENTP": {
        "title": "변론가 (ENTP)",
        "personality": "창의적이고 에너지 넘치며, 다양한 아이디어를 자유롭게 표현합니다.",
        "love": "열정적이고 유쾌한 연애를 선호하며 지적 대화에 끌립니다.",
    },
    "INFJ": {
        "title": "옹호자 (INFJ)",
        "personality": "깊은 통찰력과 공감을 기반으로 조용하지만 강한 영향력을 끼칩니다.",
        "love": "감성적 연결과 깊은 헌신을 중시하며, 진심 어린 관계를 추구합니다.",
    },
    "INFP": {
        "title": "중재자 (INFP)",
        "personality": "이상주의적이며 깊은 내면의 가치를 중시합니다.",
        "love": "감정적으로 깊게 연결되는 관계를 추구하며, 진심과 이해를 중요시합니다.",
    },
    "ENFJ": {
        "title": "선도자 (ENFJ)",
        "personality": "사람들에게 영감을 주며 타인의 성장을 돕는 데 열정적입니다.",
        "love": "상대의 감정을 존중하며 헌신적이고 따뜻한 연애를 합니다.",
    },
    "ENFP": {
        "title": "활동가 (ENFP)",
        "personality": "자유롭고 열정적이며 창의력이 풍부한 성격입니다.",
        "love": "감정 표현이 풍부하고 낭만적인 관계를 선호합니다.",
    },
    "ISTJ": {
        "title": "현실주의자 (ISTJ)",
        "personality": "책임감 있고 철저하며 전통을 중시합니다.",
        "love": "안정적이고 신뢰할 수 있는 관계를 선호하며 꾸준한 노력을 아끼지 않습니다.",
    },
    "ISFJ": {
        "title": "수호자 (ISFJ)",
        "personality": "조용하고 따뜻하며 책임감이 강한 유형입니다.",
        "love": "상대방을 배려하고 보호하려는 마음이 강하며 헌신적입니다.",
    },
    "ESTJ": {
        "title": "경영자 (ESTJ)",
        "personality": "현실적이고 체계적이며 강한 리더십을 발휘합니다.",
        "love": "연애에서도 실질적이며 책임감 있게 관계를 이끕니다.",
    },
    "ESFJ": {
        "title": "집정관 (ESFJ)",
        "personality": "사교적이고 타인의 감정에 민감하며 조화를 추구합니다.",
        "love": "정서적으로 헌신하며 상대방의 필요를 잘 챙깁니다.",
    },
    "ISTP": {
        "title": "장인 (ISTP)",
        "personality": "조용하면서도 분석적이고 문제 해결에 뛰어납니다.",
        "love": "자유로운 관계를 선호하며, 감정보다는 행동으로 표현합니다.",
    },
    "ISFP": {
        "title": "모험가 (ISFP)",
        "personality": "감성적이고 예술적인 성향을 가지며 자유로움을 중시합니다.",
        "love": "즉흥적이고 감성적인 연애를 선호하며, 따뜻한 분위기를 좋아합니다.",
    },
    "ESTP": {
        "title": "사업가 (ESTP)",
        "personality": "에너지가 넘치고 도전적인 성향으로, 현실 감각이 뛰어납니다.",
        "love": "즉흥적이고 열정적인 연애를 즐기며 감정 표현이 솔직합니다.",
    },
    "ESFP": {
        "title": "연예인 (ESFP)",
        "personality": "활달하고 사교적이며 사람들과 어울리는 것을 좋아합니다.",
        "love": "사랑을 즐기고 감정 표현이 풍부하며 상대와 즐거운 시간을 보내고 싶어합니다.",
    },
}

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 & 연애 가치관 분석기", layout="centered")

# 헤더
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>✨ MBTI 분석 웹앱 ✨</h1>", unsafe_allow_html=True)
st.markdown("### 당신의 MBTI를 입력하세요! (예: INFP, ESTJ)")

# 사용자 입력
user_input = st.text_input("MBTI 입력", max_chars=4).upper().strip()

# 결과 출력
if user_input:
    if user_input in mbti_descriptions:
        with st.spinner("당신의 MBTI 성격을 분석 중입니다... 🔍"):
            time.sleep(1.5)
        st.balloons()

        data = mbti_descriptions[user_input]
        st.markdown(f"## 🧠 성격 유형: **{data['title']}**")
        st.markdown(f"### ✔️ 성격 특성")
        st.markdown(f"{data['personality']}")
        st.markdown("---")
        st.markdown("### 💖 연애 가치관")
        st.markdown(f"{data['love']}")
        st.success("자신의 MBTI를 이해하면 더 좋은 인간관계를 만들 수 있어요 😊")

    else:
        st.error("올바른 MBTI 유형을 입력하세요 (예: INFP, ESTJ 등).")

# 부가 정보
with st.expander("💡 MBTI란 무엇인가요?"):
    st.markdown("""
        MBTI는 사람의 성격을 16가지 유형으로 분류한 성격 유형 지표입니다.  
        네 가지 차원으로 구성됩니다:
        - **외향(E)/내향(I)**  
        - **감각(S)/직관(N)**  
        - **사고(T)/감정(F)**  
        - **판단(J)/인식(P)**  
        
        MBTI를 알면 자신과 타인을 더 잘 이해할 수 있어요! 😊
    """)
