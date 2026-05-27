import streamlit as st
import time
import random  # ⭐ 선택지 무작위 셔플을 위한 라이브러리 추가

# 1. 페이지 레이아웃 및 Stop 버튼 숨기기 CSS 설정
st.set_page_config(layout="wide", page_title="국어 논리력 시한폭탄 훈련")

st.markdown("""
    <style>
    [data-testid="stStatusWidget"] button {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

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

# 4. 세션 상태 초기화 및 첫 선택지 무작위 셔플
if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = {}
    for q_id in QUIZ_DATA.keys():
        # ⭐ 각 문제의 보기 복사 후 무작위로 섞어서 저장
        shuffled_opts = QUIZ_DATA[q_id]["options"].copy()
        random.shuffle(shuffled_opts)
        
        st.session_state.quiz_state[q_id] = {
            "stage": "solving",       
            "wrong_para_warning": False,
            "result": "진행 중 ⏳",
            "mistakes": 0,
            "lockout_end_time": None, 
            "lockout_done": False,
            "shuffled_options": shuffled_opts  # ⭐ 저장된 셔플 보기
        }
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0
if "print_view" not in st.session_state:
    st.session_state.print_view = False

# ⭐ [새로고침 방지 핵심 철벽 방어선] URL 주소창에서 강제 락 정보 동기화 복구
for q_id in QUIZ_DATA.keys():
    param_key = f"lock_{q_id}"
    if param_key in st.query_params:
        end_time = float(st.query_params[param_key])
        if time.time() < end_time:
            # 새로고침을 해도 주소창 값을 읽어 강제로 타임락방 상태로 원복시킴
            st.session_state.quiz_state[q_id]["stage"] = "exploded"
            st.session_state.quiz_state[q_id]["lockout_end_time"] = end_time
            st.session_state.quiz_state[q_id]["mistakes"] = 3
            st.session_state.quiz_state[q_id]["result"] = "미션 실패 ❌"
        else:
            # 시간이 다 만료되었다면 주소창 파라미터 청소
            del st.query_params[param_key]

def go_next():
    if st.session_state.active_tab < len(QUIZ_DATA) - 1:
        st.session_state.active_tab += 1

# --- [🖨️ PDF 인쇄용 전용 화면 모드] ---
if st.session_state.print_view:
    st.header("📋 국어 독해 훈련 결과 성적표")
    st.subheader("단원: 01. 곰과 두 친구")
    
    completed_tasks = sum(1 for s in st.session_state.quiz_state.values() if s["stage"] in ["done", "exploded"])
    st.write(f"**총 {len(QUIZ_DATA)}문제 중 {completed_tasks}문제 완료**")
    
    data = []
    for q_id, info in QUIZ_DATA.items():
        res = st.session_state.quiz_state[q_id]["result"]
        data.append({"문제": f"{q_id}번", "결과": res})
    
    st.table(data)
    st.info("💡 팁: 브라우저 메뉴의 '인쇄' 또는 'Ctrl+P'를 누른 후 'PDF로 저장'을 선택하세요.")
    
    if st.button("⬅️ 학습 화면으로 돌아가기"):
        st.session_state.print_view = False
        st.rerun()
    st.stop()


# --- [💻 일반 학습 화면 모드] ---
col1, col2 = st.columns([1, 1])

current_idx = st.session_state.active_tab
q_list = list(QUIZ_DATA.keys())
current_q_id = q_list[current_idx]
active_state = st.session_state.quiz_state[current_q_id]
q_info = QUIZ_DATA[current_q_id]

all_completed = all(
    st.session_state.quiz_state[qid]["stage"] == "done" or 
    (st.session_state.quiz_state[qid]["stage"] == "exploded" and st.session_state.quiz_state[qid].get("lockout_done", False))
    for qid in QUIZ_DATA.keys()
)

# 형광펜 라이브 하이라이트 알고리즘
highlight_para_num = None
if active_state["stage"] == "step1":
    sb_value = st.session_state.get(f"sb_{current_q_id}")
    if sb_value: highlight_para_num = int(sb_value.replace("문단", ""))
elif active_state["stage"] in ["step2", "step3", "exploded"]:
    highlight_para_num = QUIZ_DATA[current_q_id]["correct_para"]

# [왼쪽 열: 지문 영역]
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

# [오른쪽 열: 문제 및 폭탄 게이지 영역]
with col2:
    st.subheader("✏️ 훈련 미션 영역")
    
    mistakes = active_state["mistakes"]
    if active_state["stage"] != "exploded":
        if mistakes == 0:
            bomb_bar = "<div style='font-size: 18px; text-align: center; background-color: #E2E8F0; padding: 10px; border-radius: 8px; margin-bottom: 15px;'>💣 🟩🟩🟩🟩🟩 🔥 <span style='font-size: 13px; color: #4A5568;'>(안전 상태)</span></div>"
        elif mistakes == 1:
            bomb_bar = "<div style='font-size: 18px; text-align: center; background-color: #FEEBC8; padding: 10px; border-radius: 8px; margin-bottom: 15px;'>💣 🟩🟩🟩🟨🟨 🔥 <span style='font-size: 13px; color: #C05621; font-weight: bold;'>(치이익- 불꽃이 타들어 갑니다!)</span></div>"
        elif mistakes == 2:
            bomb_bar = "<div style='font-size: 18px; text-align: center; background-color: #FED7D7; padding: 10px; border-radius: 8px; margin-bottom: 15px;'>💣 🟩🟨🟨🟥🟥 🔥 <span style='font-size: 13px; color: #C53030; font-weight: bold;'>(경고! 다음 오답 시 대폭발!)</span></div>"
        st.markdown(bomb_bar, unsafe_allow_html=True)

    if active_state["stage"] != "exploded":
        st.markdown(f"<div style='font-size: 18px; font-weight: bold; color: #1E3A8A; background-color: #EDF2F7; padding: 12px; border-radius: 6px; margin-bottom: 15px;'>📍 {q_info['question']}</div>", unsafe_allow_html=True)

    # --- [1차 풀이 단계] ---
    if active_state["stage"] == "solving":
        # ⭐ 셔플된 선택지(`active_state["shuffled_options"]`)를 화면에 매핑
        choice = st.radio("정답 고르기:", active_state["shuffled_options"], key=f"s_{current_q_id}")
        if st.button("정답 확인", key=f"b_{current_q_id}"):
            if choice == q_info["answer"]:
                active_state["stage"] = "done"; active_state["result"] = "1차 통과 🥇"
            else:
                active_state["stage"] = "step1"; active_state["mistakes"] = 1
            st.rerun()

    # --- [Step 1: 힌트 문단 찾기 단계] ---
    elif active_state["stage"] == "step1":
        st.error("❌ 1차 시도 오답입니다. 폭탄이 작동하기 시작했습니다!")
        st.markdown("#### 🔍 [Step 1] 힌트 문단 찾기 미션")
        c_para = st.selectbox("단서가 있는 문단 선택:", [f"{i}문단" for i in range(1, len(PARAGRAPHS)+1)], key=f"sb_{current_q_id}")
        if active_state["wrong_para_warning"]: 
            st.markdown("<div style='color: #C53030; font-weight:bold; margin-bottom:10px;'>⚠️ 다시 생각해보세요! 이 문단에는 단서가 없습니다.</div>", unsafe_allow_html=True)
        if st.button("문단 확인", key=f"bp_{current_q_id}"):
            if int(c_para.replace("문단", "")) == q_info["correct_para"]:
                active_state["stage"] = "step2"; active_state["wrong_para_warning"] = False
            else:
                active_state["wrong_para_warning"] = True
            st.rerun()

    # --- [Step 2: 2차 풀이 단계] ---
    elif active_state["stage"] == "step2":
        st.success(f"🎯 {q_info['correct_para']}문단에서 단서를 확보했습니다!")
        st.markdown("#### 📝 [Step 2] 2차 시도")
        choice2 = st.radio("다시 고르기:", active_state["shuffled_options"], key=f"r2_{current_q_id}")
        if st.button("2차 확인", key=f"br2_{current_q_id}"):
            if choice2 == q_info["answer"]:
                active_state["stage"] = "done"; active_state["result"] = "2차 통과 🥈"
            else:
                active_state["stage"] = "step3"; active_state["mistakes"] = 2
            st.rerun()

    # --- [Step 3: 3차 풀이 단계] ---
    elif active_state["stage"] == "step3":
        st.error("❌ 2차 시도 실패! 불꽃이 폭탄 바로 앞까지 도달했습니다!")
        st.markdown("#### 📝 [Step 3] 최종 시도 (마지막 탈출 기회)")
        choice3 = st.radio("다시 고르기:", active_state["shuffled_options"], key=f"r3_{current_q_id}")
        if st.button("3차 확인", key=f"br3_{current_q_id}"):
            if choice3 == q_info["answer"]:
                active_state["stage"] = "done"; active_state["result"] = "3차 통과 🥉"
            else:
                active_state["stage"] = "exploded"
                active_state["mistakes"] = 3
                active_state["result"] = "미션 실패 ❌"
                active_state["lockout_done"] = False
                # ⭐ [새로고침 방지 패치] 폭탄이 터진 시점에 웹 브라우저 주소창(Query Parameter)에도 만료 시간을 박아버림
                st.query_params[f"lock_{current_q_id}"] = str(time.time() + 60)
            st.rerun()

    # --- [💥 대폭발 및 1분 강제 잠금 타이머 모드] ---
    elif active_state["stage"] == "exploded":
        st.markdown(
            "<div style='background-color: #742A2A; color: #FFF5F5; padding: 25px; border-radius: 12px; text-align: center; border: 4px solid #E53E3E; box-shadow: 0px 4px 15px rgba(229, 62, 62, 0.5);'>"
            "<h2 style='margin: 0; font-size: 28px;'>💥 콰광!!! 대폭발!!! 💥</h2>"
            "<p style='font-size: 16px; font-weight: bold; margin-top: 10px; color: #FEB2B2;'>미션 실패! 폭탄이 완전히 터졌습니다.</p>"
            "<p style='font-size: 14px; color: #E2E8F0; margin: 0;'>왼쪽에 노란색으로 특별 표시된 <b>정답 힌트 문단</b>과 아래 문제를 1분 동안 정독하세요.</p>"
            "</div>",
            unsafe_allow_html=True
        )
        st.write("")
        
        st.markdown(f"<div style='font-size: 17px; font-weight: bold; color: #4A5568; background-color: #EDF2F7; padding: 12px; border-radius: 6px;'>📍 복습용 발문 고정: {q_info['question']}</div>", unsafe_allow_html=True)
        st.radio("선택지 복습 구역 (잠금 및 실시간 순서 무작위 변경됨):", active_state["shuffled_options"], key=f"locked_opt_{current_q_id}", disabled=True)
        st.write("")

        if active_state["lockout_end_time"] is None:
            active_state["lockout_end_time"] = time.time() + 60

        current_time = time.time()
        remaining = int(active_state["lockout_end_time"] - current_time)

        if remaining > 0:
            timer_placeholder = st.empty()
            timer_placeholder.error(f"⏳ 강제 복습 시스템 작동 중: {remaining}초 동안 새로고침 및 이탈이 차단됩니다.")
            time.sleep(1)
            st.rerun()
        else:
            active_state["lockout_done"] = True
            # 타임아웃 종료 시 주소창의 락 파라미터 자동 정리
            if f"lock_{current_q_id}" in st.query_params:
                del st.query_params[f"lock_{current_q_id}"]

        if active_state["lockout_done"]:
            st.success("🔓 1분 복습이 완료되어 타임락이 해제되었습니다!")
            
            col_retry, col_skip = st.columns(2)
            with col_retry:
                if st.button("🔄 이 문제 다시 풀기", type="primary", use_container_width=True):
                    # ⭐ [다시 풀기 패치] 패자부활 시 선택지 순서를 또 한 번 무작위로 뒤섞음!
                    new_shuffled = QUIZ_DATA[current_q_id]["options"].copy()
                    random.shuffle(new_shuffled)
                    
                    active_state["stage"] = "solving"
                    active_state["mistakes"] = 0
                    active_state["wrong_para_warning"] = False
                    active_state["result"] = "진행 중 ⏳"
                    active_state["lockout_end_time"] = None
                    active_state["lockout_done"] = False
                    active_state["shuffled_options"] = new_shuffled
                    st.rerun()
            with col_skip:
                if current_idx < len(QUIZ_DATA) - 1:
                    if st.button("다음 문제로 그냥 넘어가기 ➡️", use_container_width=True):
                        active_state["lockout_end_time"] = None
                        go_next()
                        st.rerun()

    # --- [🎉 미션 성공 완료 단계] ---
    if active_state["stage"] == "done":
        st.success(f"🎉 미션 완료! 안전하게 탈출했습니다. ({active_state['result']})")
        if current_idx < len(QUIZ_DATA) - 1:
            st.button("다음 문제로 넘어가기 ➡️", on_click=go_next)

    # --- [🖨️ 모든 훈련 완수 시 등장하는 성적표 버튼] ---
    if all_completed:
        st.write("")
        st.markdown("---")
        st.info("🏁 모든 훈련 과제가 종결되었습니다. 아래 버튼을 눌러 최종 보고서를 출력하세요.")
        if st.button("🖨️ 최종 성적표 인쇄하기 (PDF 저장)", type="primary", use_container_width=True):
            st.session_state.print_view = True
            st.rerun()

# [하단 실시간 성적표 현황판]
st.markdown("---")
st.subheader("📊 학습 현황")
cols = st.columns(len(QUIZ_DATA))
for i, qid in enumerate(QUIZ_DATA.keys()):
    with cols[i]:
        res = st.session_state.quiz_state[qid]["result"]
        if "1차" in res:
            color = "#2E7D32"; bg = "#E8F5E9"
        elif "2차" in res:
            color = "#EF6C00"; bg = "#FFF3E0"
        elif "3차" in res:
            color = "#0277BD"; bg = "#E1F5FE"
        elif "실패" in res:
            color = "#C53030"; bg = "#FFEBEE"
        else:
            color = "#616161"; bg = "#F5F5F5"
        st.markdown(f"<div style='text-align:center; border:1px solid {color}; background-color: {bg}; border-radius:5px; padding:8px; font-size:12px; font-weight:bold; color:{color};'>{qid}번<br>{res}</div>", unsafe_allow_html=True)
