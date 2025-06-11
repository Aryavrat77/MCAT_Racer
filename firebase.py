from firebase_admin import db
from firebase_config import init_firebase

# Initialize Firebase
init_firebase()

def get_room_questions(room_code):
    try:
        ref = db.reference(f"rooms/{room_code}/questions")
        questions = ref.get()
        return questions if isinstance(questions, list) else None
    except Exception as e:
        print("⚠️ Firebase read error:", e)
        return None


def set_room_questions(room_code, questions):
    ref = db.reference(f"rooms/{room_code}/questions")
    ref.set(questions)

def update_player_score(room_code, player_name, score):
    ref = db.reference(f"rooms/{room_code}/players/{player_name}")
    ref.set(score)

def get_leaderboard(room_code):
    ref = db.reference(f"rooms/{room_code}/players")
    return ref.get() or {}
