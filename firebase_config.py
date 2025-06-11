import firebase_admin
from firebase_admin import credentials, db
import os

# Firebase configuration
FIREBASE_KEY_PATH = "firebase_key.json"
FIREBASE_DB_URL = "https://mcat-quizracer-default-rtdb.firebaseio.com/"

def init_firebase():
    """
    Initialize Firebase if not already initialized.
    Returns the Firebase app instance.
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_KEY_PATH)
        return firebase_admin.initialize_app(cred, {
            'databaseURL': FIREBASE_DB_URL
        })
    return firebase_admin.get_app()

# Initialize Firebase when module is imported
firebase_app = init_firebase()
