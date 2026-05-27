import streamlit as st

# 1. 페이지 와이드 레이아웃 설정 (화면을 넓게 써서 왼쪽 지문, 오른쪽 문제를 배치)
st.set_page_config(layout="wide", page_title="국어 논리력 통합 훈련")

# 2. 본문 원문 데이터
STORY_TEXT = """절친한 두 친구가 산길을 함께 걸어가고 있었어요. 두 친구는 콩 한 쪽도 나누어 먹을 만큼 가까운 사이였어요. 두 사람이 어두운 수풀을 지나고 있는데, 갑자기 집채만 한 곰 한 마리가 나타나서 길을 막았어요. 

크고 무시무시한 곰을 보자마자, 한 친구는 냉큼 나무 위로 올라갔어요. 하지만 다른 친구는 도망갈 곳을 찾지 못했지요. 그래서 다급한 마음에 땅바닥에 납작 엎드려 죽은 척을 했어요.

곰은 땅바닥에 엎드려 죽은 척하고 있는 친구에게 다가갔어요. 그런데 이상하게도 곰은 그 친구의 귀에 대고 뭐라고 소곤소곤 속삭이더니 숲속으로 사라져 버렸어요. 곰이 사라지고 난 후 엉금엉금 나무에서 내려온 친구가 엎드려 있던 친구에게 물었어요.

“보게 친구, 괜찮은가? 그런데 곰이 자네 귀에다 무슨 말을 속삭이던가?”

엎드려 있던 친구가 먼지를 툭툭 털고 일어나며 말했어요.

“위험에 처했을 때 혼자 살려고 도망가는 친구는 진정한 친구가 아니라고 하더군.”

이 이야기는 ‘어려울 때 도와주는 친구가 진정한 친구’라는 교훈을 담고 있습니다."""

# 3. 교재 1번~7번 전체 문제 데이터 세팅
QUIZ_DATA = {
    1: {
        "question": "1. 절친한 두 친구는 어디를 걸어가고 있었나요?",
        "options": ["① 정글", "② 광장", "③ 들판", "④ 산길", "⑤ 해변"],
        "answer": "④ 산길",
        "clue": "산길"
    },
    2: {
        "question": "2. 두 친구는 어떤 사이였나요?",
        "options": [
            "① 누가 잘 달리는지 다투는 사이", 
            "② 같은 마을에서 함께 자란 사이", 
            "③ 콩 한 쪽도 나누어 먹는 가까운 사이", 
            "④ 말하지 않아도 서로의 마음을 아는 사이", 
            "⑤ 서로 잘 되는 것을 보면 배가 아픈 사이"
        ],
        "answer": "③ 콩 한 쪽도 나누어 먹는 가까운 사이",
        "clue": "콩 한 쪽도 나누어 먹을 만큼 가까운 사이"
    },
    3: {
        "question": "3. 곰이 나타나자 한 친구는 어디로 도망갔나요?",
        "options": ["① 동굴 속", "② 바위 뒤", "③ 나무 위", "④ 수풀 안", "⑤ 계곡 옆"],
        "answer": "③ 나무 위",
        "clue": "나무 위"
    },
    4: {
        "question": "4. 다급해진 다른 친구는 그 자리에서 어떻게 하였나요?",
        "options": [
            "① 노래를 부르며 곰을 진정시켰다.",
            "② 땅바닥에 납작 엎드려 죽은 척했다.",
            "③ 곰의 눈을 쳐다보며 절대 물러나지 않았다.",
            "④ 나무처럼 손을 들고 서서 곰이 갈 때까지 기다렸다.",
            "⑤ 친구에게 도와 달라고 소리 질렀다."
        ],
        "answer": "② 땅바닥에 납작 엎드려 죽은 척했다.",
        "clue": "땅바닥에 납작 엎드려 죽은 척을 했어요"
    },
    5: {
        "question": "5. 곰은 도망가지 못한 친구에게 어떻게 하였나요?",
        "options": [
            "① 귀에 대고 뭐라고 속삭이더니 사라졌다.",
            "② 쳐다보기만 하고 가던 길을 계속 갔다.",
            "<b>③ 친구의 뺨을 핥으며 같이 놀자고 했다.</b>", # 이미지 텍스트 반영
            "④ 커다란 앞발로 친구를 날려 버렸다.",
            "⑤ 친구를 등에 태우고 산길을 올라갔다."
        ],
        "answer": "① 귀에 대고 뭐라고 속삭이더니 사라졌다.",
        "clue": "귀에 대고 뭐라고 소곤소곤 속삭이더니"
    },
    6: {
        "question": "6. 도망간 친구는 도망가지 못한 친구에게 뭐라고 말했나요?",
        "options": [
            "① 다음부터는 날 따라 나오지 말고 집에 있게!",
            "② 이 친구야, 빨리빨리 좀 움직이지 못하겠나?",
            "③ 하늘이 도왔구먼, 이렇게 멀쩡한 걸 보니!",
            "④ 곰이 자네 귀에다 무슨 말을 속삭이던가?",
            "⑤ 곰을 직접 보니 어떤 느낌이었나?"
        ],
        "answer": "④ 곰이 자네 귀에다 무슨 말을 속삭이던가?",
        "clue": "곰이 자네 귀에다 무슨 말을 속삭이던가?"
    },
    7: {
        "question": "7. 이 이야기의 교훈은 무엇인가요?",
        "options": [
            "① 남을 먼저 생각하는 마음을 가져야 한다.",
            "② 진정한 친구는 어려울 때 도와주는 친구이다.",
            "③ 무엇이든 꾸준히 노력하면 안 되는 것이 없다.",
            "④ 조금씩 모으다 보면 언젠가 큰 것이 된다.",
            "⑤ 어릴 적 습관은 늙어서까지 계속된다."
        ],
        "answer": "② 진정한 친구는 어려울 때 도와주는 친구이다.",
        "clue": "‘어려울 때 도와주는 친구가 진정한 친구’라는 교훈"
    }
}

# 세션 상태 초기화
if "results" not in st.session_state:
    st.session_state.results = {}
if "current_clue" not in st.session_state:
    st.session_state.current_clue = None

# 타이틀 부분
st.title("📖 국어 문법·독해 논리력 완전학습 훈련")
st.caption("지문을 먼저 정독한 뒤 문제를 풀어보세요. 틀린 문제는 왼쪽 지문에서 단서가 하이라이트됩니다.")
st.markdown("---")

# 화면을 두 개의 열(Column)로 분할
col1, col2 = st.columns([1, 1])

# [왼쪽 열: 교재 지문 상시 고정 영역]
with col1:
    st.subheader("📜 01. 곰과 두 친구 (본문)")
    
    # 하이라이트할 단서가 있다면 처리
    display_story = STORY_TEXT
    if st.session_state.current_clue:
        clue = st.session_state.current_clue
        display_story = display_story.replace(
            clue, 
            f"<mark style='background-color: #FFEB3B; color: black; font-weight: bold; padding: 2px 4px; rouded: 4px;'>{clue}</mark>"
        )
        st.warning("⚠️ 오른쪽 문제의 단서가 아래 본문에 노란색으로 표시되었습니다. 다시 읽고 풀어보세요!")

    # 본문 박스 형태로 출력
    st.markdown(
        f"<div style='background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 5px solid #007BFF; line-height: 1.8; font-size: 16px; color: #333333;'>"
        f"{display_story.replace('\n', '<br>')}"
        f"</div>", 
        unsafe_allow_html=True
    )

# [오른쪽 열: 문제 풀이 영역]
with col2:
    st.subheader("✏️ 문제풀이 단원")
    
    # 1번부터 7번까지 탭(Tab) 구절로 만들어 아이들이 집중도 있게 한 문제씩 풀도록 유도
    tabs = st.tabs([f"{i}번" for i in QUIZ_DATA.keys()])
    
    for idx, (q_id, q_info) in enumerate(QUIZ_DATA.items()):
        with tabs[idx]:
            st.markdown(f"#### {q_info['question']}")
            user_choice = st.radio("정답을 고르세요:", q_info["options"], key=f"q_{q_id}")
            
            # 버튼 클릭 이벤트
            if st.button("정답 확인하기", key=f"btn_{q_id}"):
                if user_choice == q_info["answer"]:
                    st.session_state.results[q_id] = "correct"
                    # 정답이면 하이라이트 제거 혹은 초기화
                    if st.session_state.current_clue == q_info["clue"]:
                        st.session_state.current_clue = None
                    st.rerun()
                else:
                    st.session_state.results[q_id] = "incorrect"
                    # 틀리면 왼쪽 지문에 단서 표시되도록 세팅
                    st.session_state.current_clue = q_info["clue"]
                    st.rerun()
            
            # 문제별 결과 알림 메시지
            if q_id in st.session_state.results:
                if st.session_state.results[q_id] == "correct":
                    st.success("🎉 정답입니다! 본문 내용을 아주 잘 이해했네요.")
                else:
                    st.error("❌ 오답입니다. 왼쪽 본문에서 노랗게 반짝이는 단서 문장을 찾아 다시 읽어보세요!")
