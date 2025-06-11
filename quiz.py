import streamlit as st
import time
from firebase import get_room_questions, set_room_questions, update_player_score, get_leaderboard
import random
from firebase_config import init_firebase
init_firebase()

class QuizSession:
    def __init__(self, player_name, room_code, all_questions):
        self.player_name = player_name
        self.room_code = room_code
        self.key_prefix = f"{self.player_name}_{self.room_code}_"
        self.questions = all_questions
        self.total_questions = len(all_questions)
        
        # Initialize session state
        self._init_session_state()
        
        # Load or create shared questions
        self._setup_questions()

    def _init_session_state(self):
        """Initialize all session state variables"""
        if f"{self.key_prefix}score" not in st.session_state:
            st.session_state[f"{self.key_prefix}score"] = 0
        if f"{self.key_prefix}q_index" not in st.session_state:
            st.session_state[f"{self.key_prefix}q_index"] = 0
        if f"{self.key_prefix}finished" not in st.session_state:
            st.session_state[f"{self.key_prefix}finished"] = False

    def _setup_questions(self):
        """Load or create shared questions"""
        shared_questions = get_room_questions(self.room_code)
        if not shared_questions:
            shared_questions = random.sample(self.questions, len(self.questions))
            set_room_questions(self.room_code, shared_questions)
        
        self.quiz_questions = shared_questions
        st.session_state[f"{self.key_prefix}questions"] = shared_questions

    def _display_leaderboard(self):
        """Display the current leaderboard"""
        leaderboard = get_leaderboard(self.room_code)
        if leaderboard:
            st.markdown("### 🏆 Leaderboard")
            sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
            for name, score in sorted_board:
                st.markdown(f"- **{name}**: {score}/{self.total_questions}")

    def run(self):
        score = st.session_state[f"{self.key_prefix}score"]
        q_index = st.session_state[f"{self.key_prefix}q_index"]
        finished = st.session_state[f"{self.key_prefix}finished"]
        questions = st.session_state[f"{self.key_prefix}questions"]

        if finished:
            st.success(f"{self.player_name}, your score: {score}/{self.total_questions}")
            st.balloons()
        else:
            question = questions[q_index]
            st.subheader(f"Question {q_index + 1} of {self.total_questions}")
            choice = st.radio(question["question"], question["options"], key=f"choice_{self.key_prefix}{q_index}")

            if st.button("Submit Answer", key=f"submit_{self.key_prefix}{q_index}"):
                if choice == question["answer"]:
                    st.session_state[f"{self.key_prefix}score"] += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! Correct answer: {question['answer']}")

                st.session_state[f"{self.key_prefix}q_index"] += 1
                if st.session_state[f"{self.key_prefix}q_index"] >= self.total_questions:
                    st.session_state[f"{self.key_prefix}finished"] = True

                # Update Firebase leaderboard
                update_player_score(self.room_code, self.player_name, st.session_state[f"{self.key_prefix}score"])

                time.sleep(1)
                st.rerun()

        # Progress bar
        progress = score / self.total_questions
        st.progress(progress, text=f"Progress: {score}/{self.total_questions}")

        # Show leaderboard
        self._display_leaderboard()
