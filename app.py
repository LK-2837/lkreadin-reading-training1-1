import streamlit as st

# 1. 페이지 레이아웃 설정
st.set_page_config(layout="wide", page_title="국어 논리력 추적 완전학습")

# 2. 본문 문단별 데이터
PARAGRAPHS = [
    "절친한 두 친구가 산길을 함께 걸어가고 있었어요. 두 친구는 콩 한 쪽도 나누어 먹을 만큼 가까운 사이였어요. 두 사람이 어두운 수풀을 지나고 있는데, 갑자기 집채만 한 곰 한 마리가 나타나서 길을 막았어요.",
    "크고 무시무시한 곰을 보자마자, 한 친구는 냉큼 나무 위로 올라갔어요. 하지만 다른 친구는 도망갈 곳을 찾지 못했지요. 그래서 다급한 마음에 땅바닥에 납작 엎드려 죽은 척을 했어요.",
    "곰은 땅바닥에 엎드려 죽은 척하고 있는 친구에게 다가갔어요. 그런데 이상하게도 곰은 그 친구의 귀에 대고 뭐라고 소곤소곤 속삭이더니 숲속으로 사라져 버렸어요. 곰이 사라지고 난 후 엉금엉금 나무에서 내려온 친구가 엎드려 있던 친구에게 물었어요.",
    "“보게 친구, 괜찮은가? 그런데 곰이 자네 귀에다 무슨 말을 속삭이던가?”",
    "엎드려 있던 친구가 먼지를 툭툭 털고 일어나며 말했어요.",
    "“위험에 처했을 때 혼자 살려고 도망가는 친구는 진정한 친구가 아니라고 하더군.”",
    "이 이야기는 ‘어려울 때 도와주는 친구가 진정한 친구’라는 교훈을 담고 있습니다."
]

# 3. 문제 데이터
QUIZ_DATA = {
    1: {"question": "1. 절친한 두 친구는 어디를 걸어가고 있었나요?", "options": ["① 정글", "② 광장", "③ 들판", "④ 산길", "⑤ 해변"], "answer": "④ 산길", "correct_para": 1},
    2: {"question": "2. 두 친구는 어떤 사이였나요?", "options": ["① 누가 잘 달리는지 다투는 사이", "② 같은 마을에서 함께 자란 사이", "③ 콩 한 쪽도 나누어 먹는 가까운 사이", "④ 말하지 않아도 서로의 마음을 아는 사이", "⑤ 서로 잘 되는 것을 보면 배가 아픈 사이"], "answer": "③ 콩 한 쪽도 나누어 먹는 가까운 사이", "correct_para": 1},
    3: {"question": "3. 곰이 나타나자 한 친구는 어디로 도망갔나요?", "options": ["① 동굴 속", "② 바위 뒤", "③ 나무 위", "④ 수풀 안", "⑤ 계곡 옆"], "answer": "③ 나무 위", "correct_para": 2},
    4: {"question": "4. 다급해진 다른 친구는 그 자리에서 어떻게 하였나요?", "options": ["① 노래를 부르며 곰을 진정시켰다.", "② 땅바닥에 납작 엎드려 죽은 척했다.", "③ 곰의 눈을 쳐다보며 절대 물러나지 않았다.", "④ 나무처럼 손을 들고 서서 곰이 갈 때까지 기다렸다.", "⑤ 친구에게 도와 달라고 소리 질렀다."], "answer": "② 땅바닥에 납작 엎드려 죽은 척했다.", "correct_para": 2},
    5: {"question": "5. 곰은 도망가지 못한 친구에게 어떻게 하였나요?", "options": ["① 귀에 대고 뭐라고 속삭이더니 사라졌다.", "② 쳐다보기만 하고 가던 길을 계속 갔다.", "③ 친구의 뺨을 핥으며 같이 놀자고 했다.", "④ 커다란 앞발로 친구를 날려 버렸다.", "⑤ 친구를 등에 태우고 산길을 올라갔다."], "answer": "① 귀에 대고 뭐라고 속삭이더니 사라졌다.", "correct_para": 3},
    6: {"question": "6. 도망간 친구는 도망가지 못한 친구에게 뭐라고 말했나요?", "options": ["① 다음부터는 날 따라 나오지 말고 집에 있게!", "② 이 친구야, 빨리빨리 좀 움직이지 못하겠나?", "③ 하늘이 도왔구먼, 이렇게 멀쩡한 걸 보니!", "④ 곰이 자네 귀에다 무슨 말을 속삭이던가?", "⑤ 곰을 직접 보니 어떤 느낌이었나?"], "answer": "④ 곰이 자네 귀에다 무슨 말을 속삭이던가?", "correct_para": 4},
    7: {"question": "7. 이 이야기의 교훈은 무엇인가요?", "options": ["① 남을 먼저 생각하는 마음을 가져야 한다.", "② 진정한 친구는 어려울 때 도와주는 친구이다.", "③ 무엇이든 꾸준히 노력하면 안 되는 것이 없다.", "④ 조금씩 모으다 보면 언젠가 큰 것이 된다.", "⑤ 어릴 적 습관은 늙어서까지 계속된다."], "answer": "② 진정한 친구는 어려울 때 도와주는 친구이다.", "correct_para": 7}
}

# 세션 상태 초기화
if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = {
        q_id: {"stage": "solving", "wrong_para_warning": False, "result": "진행 중 ⏳"} for q_id in QUIZ_DATA.keys()
    }
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0  # 0~6 인덱스

def go_next():
    if st.session_state.active_tab < len(QUIZ_DATA) - 1:
        st.session_state.active_tab += 1

# [PDF 인쇄용 화면 로직]
if st.sidebar.button("🖨️ 최종 성적표 인쇄하기"):
    st.balloons()
    st.header("📋 국어 독해 훈련 결과 성적표")
    st.subheader("단원: 01. 곰과 두 친구")
    
    total_score = sum(1 for s in st.session_state.quiz_state.values() if "done" in s["stage"])
    st.write(f"**총 {len(QUIZ_DATA)}문제 중 {total_score}문제 완료**")
    
    data = []
    for q_id, info in QUIZ_DATA.items():
        res = st.session_state.quiz_state[q_id]["result"]
        data.append({"문제": f"{q_id}번", "결과": res})
    
    st.table(data)
    st.info("💡 팁: 브라우저 메뉴의 '인쇄' 또는 'Ctrl+P'를 누른 후 'PDF로 저장'을 선택하세요.")
    if st.button("돌아가기"):
        st.rerun()
    st.stop()

st.title("🚀 국어 독해 논리력 단계별 완전학습")
st.caption("문제를 틀리면 힌트 문단을 스스로 찾아야 합니다. 모든 문제를 통과하고 성적표를 출력해 보세요!")

col1, col2 = st.columns([1, 1])

# 현재 활성화된 탭 기반 문제 번호
q_list = list(QUIZ_DATA.keys())
current_q_id = q_list[st.session_state.active_tab]
active_state = st.session_state.quiz_state[current_q_id]

# 형광펜 라이브 하이라이트
highlight_para_num = None
if active_state["stage"] == "step1":
    sb_value = st.session_state.get(f"sb_{current_q_id}")
    if sb_value: highlight_para_num = int(sb_value.replace("문단", ""))
elif active_state["stage"] in ["step2", "step3"]:
    highlight_para_num = QUIZ_DATA[current_q_id]["correct_para"]

with col1:
    st.subheader("📜 01. 곰과 두 친구 (본문)")
    story_html = ""
    for idx, para in enumerate(PARAGRAPHS):
        p_num = idx + 1
        if p_num == highlight_para_num:
            story_html += f"<div style='background-color: #FFF9C4; padding: 12px; border-radius: 5px; margin-bottom: 10px; border-left: 5px solid #FBC02D; font-size:16px; color: black; font-weight: bold;'><b>[{p_num}문단]</b> {para}</div>"
        else:
            story_html += f"<div style='padding: 12px; margin-bottom: 10px; font-size:16px; color:#333;'><b>[{p_num}문단]</b> {para}</div>"
    st.markdown(f"<div style='background-color: #F8F9FA; padding: 15px; border-radius: 10px; border: 1px solid #E0E0E0;'>{story_html}</div>", unsafe_allow_html=True)

with col2:
    st.subheader("✏️ 훈련 미션 영역")
    
    # 세션 상태와 연동된 탭 (st.tabs 대신 인덱스 기반의 수동 탭 구현 효과)
    current_idx = st.session_state.active_tab
    q_id = q_list[current_idx]
    state = st.session_state.quiz_state[q_id]
    q_info = QUIZ_DATA[q_id]

    st.markdown(f"### 📍 {q_info['question']}")
    st.markdown("---")

    # [단계별 로직]
    if state["stage"] == "solving":
        choice = st.radio("정답 고르기:", q_info["options"], key=f"s_{q_id}")
        if st.button("정답 확인", key=f"b_{q_id}"):
            if choice == q_info["answer"]:
                state["stage"] = "done"; state["result"] = "1차 통과 🥇"
                st.rerun()
            else:
                state["stage"] = "step1"; st.rerun()

    elif state["stage"] == "step1":
        st.error("❌ 오답입니다. 단서 문단을 찾아보세요.")
        st.markdown("#### 🔍 [Step 1] 힌트 문단 찾기")
        c_para = st.selectbox("문단 선택:", [f"{i}문단" for i in range(1, len(PARAGRAPHS)+1)], key=f"sb_{q_id}")
        if state["wrong_para_warning"]: st.warning("⚠️ 다시 생각해보세요! 이 문단에는 단서가 없습니다.")
        if st.button("문단 확인", key=f"bp_{q_id}"):
            if int(c_para.replace("문단", "")) == q_info["correct_para"]:
                state["stage"] = "step2"; state["wrong_para_warning"] = False
            else:
                state["wrong_para_warning"] = True
            st.rerun()

    elif state["stage"] == "step2":
        st.success(f"🎯 {q_info['correct_para']}문단에서 단서를 찾았습니다!")
        st.markdown("#### 📝 [Step 2] 2차 시도")
        choice2 = st.radio("다시 고르기:", q_info["options"], key=f"r2_{q_id}")
        if st.button("2차 확인", key=f"br2_{q_id}"):
            if choice2 == q_info["answer"]:
                state["stage"] = "done"; state["result"] = "2차 통과 🥈"
            else:
                state["stage"] = "step3"
            st.rerun()

    elif state["stage"] == "step3":
        st.error("❌ 마지막 기회입니다.")
        st.markdown("#### 📝 [Step 3] 최종 시도")
        choice3 = st.radio("다시 고르기:", q_info["options"], key=f"r3_{q_id}")
        if st.button("3차 확인", key=f"br3_{q_id}"):
            if choice3 == q_info["answer"]:
                state["stage"] = "done"; state["result"] = "3차 통과 🥉"
            else:
                st.error("❌ 정답이 아닙니다. 형광펜 문단을 다시 정독해 보세요.")
            st.rerun()

    if state["stage"] == "done":
        st.success(f"🎉 미션 완료! ({state['result']})")
        if current_idx < len(QUIZ_DATA) - 1:
            st.button("다음 문제로 넘어가기 ➡️", on_click=go_next)
        else:
            st.info("🏁 마지막 문제까지 모두 완료했습니다! 사이드바에서 성적표를 출력하세요.")

# [하단 실시간 성적표]
st.markdown("---")
st.subheader("📊 학습 현황")
cols = st.columns(len(QUIZ_DATA))
for i, qid in enumerate(QUIZ_DATA.keys()):
    with cols[i]:
        res = st.session_state.quiz_state[qid]["result"]
        color = "#2E7D32" if "1차" in res else ("#EF6C00" if "2차" in res else ("#0277BD" if "3차" in res else "#616161"))
        st.markdown(f"<div style='text-align:center; border:1px solid {color}; border-radius:5px; padding:5px; font-size:12px; font-weight:bold; color:{color};'>{qid}번<br>{res}</div>", unsafe_allow_html=True)
