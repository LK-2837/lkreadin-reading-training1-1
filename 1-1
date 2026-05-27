import streamlit as st

# 1. 본문 데이터 세팅
STORY_TEXT = """절친한 두 친구가 산길을 함께 걸어가고 있었어요. 두 친구는 콩 한 쪽도 나누어 먹을 만큼 가까운 사이였어요. 두 사람이 어두운 수풀을 지나고 있는데, 갑자기 집채만 한 곰 한 마리가 나타나서 길을 막았어요. 

크고 무시무시한 곰을 보자마자, 한 친구는 냉큼 나무 위로 올라갔어요. 하지만 다른 친구는 도망갈 곳을 찾지 못했지요. 그래서 다급한 마음에 땅바닥에 납작 엎드려 죽은 척을 했어요.

곰은 땅바닥에 엎드려 죽은 척하고 있는 친구에게 다가갔어요. 그런데 이상하게도 곰은 그 친구의 귀에 대고 뭐라고 소곤소곤 속삭이더니 숲속으로 사라져 버렸어요. 곰이 사라지고 난 후 엉금엉금 나무에서 내려온 친구가 엎드려 있던 친구에게 물었어요.

“보게 친구, 괜찮은가? 그런데 곰이 자네 귀에다 무슨 말을 속삭이던가?”

엎드려 있던 친구가 먼지를 툭툭 털고 일어나며 말했어요.

“위험에 처했을 때 혼자 살려고 도망가는 친구는 진정한 친구가 아니라고 하더군.”

이 이야기는 ‘어려울 때 도와주는 친구가 진정한 친구’라는 교훈을 담고 있습니다."""

# 2. 문제 및 단서 매칭 데이터 세팅
QUIZ_DATA = {
    1: {
        "question": "1. 절친한 두 친구는 어디를 걸어가고 있었나요?",
        "options": ["① 정글", "② 광장", "③ 들판", "④ 산길", "⑤ 해변"],
        "answer": "④ 산길",
        "clue": "산길"
    },
    2: {
        "question": "2. 두 친구는 어떤 사이였나요?",
        "options": ["① 누가 잘 달리는지 다투는 사이", "② 같은 마을에서 함께 자란 사이", "③ 콩 한 쪽도 나누어 먹는 가까운 사이", "④ 말하지 않아도 서로의 마음을 아는 사이", "⑤ 서로 잘 되는 것을 보면 배가 아픈 사이"],
        "answer": "③ 콩 한 쪽도 나누어 먹는 가까운 사이",
        "clue": "콩 한 쪽도 나누어 먹을 만큼 가까운 사이"
    },
    3: {
        "question": "3. 곰이 나타나자 한 친구는 어디로 도망갔나요?",
        "options": ["① 동굴 속", "② 바위 뒤", "③ 나무 위", "④ 수풀 안", "⑤ 계곡 옆"],
        "answer": "③ 나무 위",
        "clue": "나무 위"
    }
}

st.title("📖 국어 논리력 통합 훈련 - 근거 추적 프로그램")
st.caption("정답을 틀리면 책 속에서 논리적 단서가 있는 문장을 찾아줍니다.")
st.markdown("---")

# 세션 상태 초기화 (문제별 풀이 상태 저장)
if "results" not in st.session_state:
    st.session_state.results = {}

# 문제 출력 및 로직 작동
for q_id, q_info in QUIZ_DATA.items():
    st.subheader(f"📍 문제 {q_id}")
    user_choice = st.radio(q_info["question"], q_info["options"], key=f"q_{q_id}")
    
    if st.button(f"{q_id}번 정답 확인", key=f"btn_{q_id}"):
        if user_choice == q_info["answer"]:
            st.session_state.results[q_id] = {"status": "correct"}
        else:
            st.session_state.results[q_id] = {"status": "incorrect", "clue": q_info["clue"]}

    # 결과 화면 표시 (이 부분이 핵심 논리 엔진입니다)
    if q_id in st.session_state.results:
        res = st.session_state.results[q_id]
        if res["status"] == "correct":
            st.success("🎉 정답입니다! 훌륭한 독해 능력을 가지고 있군요.")
        else:
            st.error("❌ 오답입니다. 우리가 읽은 책 속에서 단서를 다시 찾아볼까요?")
            
            # 본문에서 단서 문장을 찾아서 노란색 하이라이팅(<mark>) 처리
            clue_text = res["clue"]
            highlighted_story = STORY_TEXT.replace(clue_text, f"<mark style='background-color: #FFEB3B; color: black; font-weight: bold;'>{clue_text}</mark>")
            
            with st.expander("🔍 본문 속 논리적 단서 확인하기 (펼쳐보세요)", expanded=True):
                st.write("아래 하이라이트된 문장을 읽고 다시 생각해 보세요!")
                # HTML 태그를 인식하여 화면에 렌더링
                st.markdown(highlighted_story.replace("\n", "<br>"), unsafe_allow_value=True)
    st.markdown("---")
