# main.py
import streamlit as st
from quiz import QuizSession
from questions import QUESTIONS

st.set_page_config(page_title="MCAT QuizRacer MVP", layout="centered")
st.title("🏁 MCAT QuizRacer")
st.write("Race through MCAT questions. Get points. Beat your friends.")

# Player setup
player_name = st.text_input("Enter your name:")
room_code = st.text_input("Enter room code:")

if player_name and room_code:
    session = QuizSession(player_name, room_code, QUESTIONS)
    session.run()
else:
    st.info("Enter your name and room code to join the game.")
