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

# 3. 전체 문제 및 문단 매칭 데이터
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
        q_id: {
            "stage": "solving",       # solving -> step1 -> step2 -> step3 -> done
            "wrong_para_warning": False,
            "result": "진행 중 ⏳"
        } for q_id in QUIZ_DATA.keys()
    }
if "last_active_q" not in st.session_state:
    st.session_state.last_active_q = 1

# 셀렉트박스 변경 시 현재 어떤 문제를 건드리고 있는지 저장하는 함수
def update_active_q(q_id):
    st.session_state.last_active_q = q_id

st.title("🚀 국어 독해 논리력 단계별 완전학습")
st.caption("틀린 문제는 스스로 힌트 문단을 찾고 고쳐 풀며 3차 통과를 목표로 도전해 보세요!")
st.markdown("---")

# 레이아웃 분할
col1, col2 = st.columns([1, 1])

# 현재 활성화된 문제와 상태 파악
active_q = st.session_state.last_active_q
active_state = st.session_state.quiz_state[active_q]

# 형광펜을 칠할 문단 번호 결정 로직 (Live Highlight)
highlight_para_num = None
if active_state["stage"] == "step1":
    # 학생이 현재 셀렉트박스에서 선택하고 있는 문단 번호를 즉시 반영
    sb_value = st.session_state.get(f"sb_{active_q}")
    if sb_value:
        highlight_para_num = int(sb_value.replace("문단", ""))
elif active_state["stage"] in ["step2", "step3"]:
    # 정답 문단을 맞춘 상태면 정답 문단을 고정 하이라이트
    highlight_para_num = QUIZ_DATA[active_q]["correct_para"]

# [왼쪽 열: 지문 상시 고정 및 실시간 형광펜]
with col1:
    st.subheader("📜 01. 곰과 두 친구 (본문)")
    story_html = ""
    for idx, para in enumerate(PARAGRAPHS):
        para_num = idx + 1
        if para_num == highlight_para_num:
            # 선택된 문단은 노란색 형광펜 효과
            story_html += f"<div style='background-color: #FFF9C4; padding: 12px; border-radius: 5px; margin-bottom: 10px; border-left: 5px solid #FBC02D; font-size:16px; line-height:1.8; color: black; font-weight: bold;'><b>[{para_num}문단]</b> {para}</div>"
        else:
            story_html += f"<div style='padding: 12px; margin-bottom: 10px; font-size:16px; line-height:1.8; color:#333333;'><b>[{para_num}문단]</b> {para}</div>"
            
    st.markdown(f"<div style='background-color: #F8F9FA; padding: 15px; border-radius: 10px; border: 1px solid #E0E0E0;'>{story_html}</div>", unsafe_allow_html=True)

# [오른쪽 열: 문제 풀이 및 단계별 미션]
with col2:
    st.subheader("✏️ 훈련 미션 단원")
    tabs = st.tabs([f"{i}번 문제" for i in QUIZ_DATA.keys()])
    
    for idx, (q_id, q_info) in enumerate(QUIZ_DATA.items()):
        with tabs[idx]:
            # 탭을 클릭하거나 조작할 때 해당 문제를 활성화
            state = st.session_state.quiz_state[q_id]
            
            # --- [1차 풀이 단계] ---
            if state["stage"] == "solving":
                st.markdown(f"#### {q_info['question']}")
                user_choice = st.radio("정답을 고르세요:", q_info["options"], key=f"select_{q_id}", on_change=update_active_q, args=(q_id,))
                
                if st.button("정답 확인", key=f"btn_solve_{q_id}"):
                    update_active_q(q_id)
                    if user_choice == q_info["answer"]:
                        state["stage"] = "done"
                        state["result"] = "1차 통과 🥇"
                        st.rerun()
                    else:
                        state["stage"] = "step1"
                        st.rerun()
            
            # --- [Step 1: 힌트 문단 찾기 단계 - 잘못 고르면 경고] ---
            elif state["stage"] == "step1":
                st.error("❌ 1차 시도 오답입니다.")
                st.markdown("### 🔍 [Step 1] 힌트 문단 찾기 미션")
                st.info("오른쪽에서 문단을 변경하면 왼쪽에 자동으로 형광펜이 칠해집니다. 단서가 있는 문단을 찾아보세요!")
                
                chosen_para = st.selectbox(
                    "힌트 문단 선택:", 
                    options=[f"{i}문단" for i in range(1, len(PARAGRAPHS)+1)], 
                    key=f"sb_{q_id}",
                    on_change=update_active_q,
                    args=(q_id,)
                )
                
                if state["wrong_para_warning"]:
                    st.warning("⚠️ 다시 생각해보세요! 선택한 문단에는 정답의 결정적 단서가 없습니다.")
                
                if st.button("문단 확인", key=f"btn_para_{q_id}"):
                    update_active_q(q_id)
                    para_int = int(chosen_para.replace("문단", ""))
                    if para_int == q_info["correct_para"]:
                        state["stage"] = "step2"
                        state["wrong_para_warning"] = False
                        st.rerun()
                    else:
                        state["wrong_para_warning"] = True
                        st.rerun()
            
            # --- [Step 2: 2차 풀이 단계] ---
            elif state["stage"] == "step2":
                st.success(f"🎯 대단해요! {q_info['correct_para']}문단에서 단서를 찾아냈군요!")
                st.markdown("### 📝 [Step 2] 2차 시도 - 정답 고치기")
                
                st.markdown(f"#### {q_info['question']}")
                user_choice_2 = st.radio("정답을 다시 고르세요:", q_info["options"], key=f"retry2_{q_id}", on_change=update_active_q, args=(q_id,))
                
                if st.button("2차 확인", key=f"btn_retry2_{q_id}"):
                    update_active_q(q_id)
                    if user_choice_2 == q_info["answer"]:
                        state["stage"] = "done"
                        state["result"] = "2차 통과 🥈"
                        st.rerun()
                    else:
                        state["stage"] = "step3"
                        st.rerun()
            
            # --- [Step 3: 3차 풀이 단계] ---
            elif state["stage"] == "step3":
                st.error("❌ 2차 시도도 아쉽게 틀렸습니다.")
                st.markdown("### 📝 [Step 3] 3차 시도 - 최종 기회")
                st.warning("형광펜 칠해진 문단을 단어 하나하나 소리 내어 읽어보고 마지막으로 골라보세요.")
                
                st.markdown(f"#### {q_info['question']}")
                user_choice_3 = st.radio("정답을 다시 고르세요:", q_info["options"], key=f"retry3_{q_id}", on_change=update_active_q, args=(q_id,))
                
                if st.button("3차 확인", key=f"btn_retry3_{q_id}"):
                    update_active_q(q_id)
                    if user_choice_3 == q_info["answer"]:
                        state["stage"] = "done"
                        state["result"] = "3차 통과 🥉"
                        st.rerun()
                    else:
                        st.error("❌ 아직 오답입니다. 다시 집중해서 읽어봅시다!")

            # --- [최종 완료 단계] ---
            elif state["stage"] == "done":
                st.success(f"🎉 미션 완료! 이 문제는 [{state['result']}] 상태입니다.")

# 4. 화면 하단 실시간 성적표 대시보드
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.header("📊 실시간 학습 성적표")
st.caption("스스로 단서를 추적해 원킬 통과(1차 통과)를 늘려보세요!")

# 성적표를 가로로 깔끔하게 배치하기 위한 컬럼 구성
report_cols = st.columns(len(QUIZ_DATA))
for idx, q_id in enumerate(QUIZ_DATA.keys()):
    with report_cols[idx]:
        q_res = st.session_state.quiz_state[q_id]["result"]
        
        # 패스 단계별 색상 디자인 부여
        if "1차" in q_res:
            bg_color = "#E8F5E9" # 초록
            text_color = "#2E7D32"
        elif "2차" in q_res:
            bg_color = "#FFF3E0" # 주황
            text_color = "#EF6C00"
        elif "3차" in q_res:
            bg_color = "#E1F5FE" # 파랑
            text_color = "#0277BD"
        else:
            bg_color = "#F5F5F5" # 회색 (진행 중)
            text_color = "#616161"
            
        st.markdown(
            f"<div style='background-color: {bg_color}; padding: 15px; border-radius: 8px; text-align: center; border: 1px solid {text_color};'>"
            f"<p style='margin: 0; font-size: 14px; color: #555555; font-weight: bold;'>{q_id}번 문제</p>"
            f"<p style='margin: 5px 0 0 0; font-size: 16px; color: {text_color}; font-weight: bold;'>{q_res}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
