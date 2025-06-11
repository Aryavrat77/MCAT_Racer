import firebase_admin
from firebase_admin import credentials, db
import os
import streamlit as st

# Firebase configuration
FIREBASE_DB_URL = "https://mcat-quizracer-default-rtdb.firebaseio.com/"

def init_firebase():
    """
    Initialize Firebase if not already initialized.
    Returns the Firebase app instance.
    """
    if not firebase_admin._apps:
        try:
            # Try to get credentials from Streamlit secrets
            if 'firebase' in st.secrets:
                cred = credentials.Certificate(st.secrets['firebase'])
            else:
                # Fallback to local file
                cred = credentials.Certificate("firebase_key.json")
            
            return firebase_admin.initialize_app(cred, {
                'databaseURL': FIREBASE_DB_URL
            })
        except Exception as e:
            print("⚠️ Error initializing Firebase:", e)
            raise
    return firebase_admin.get_app()

# Initialize Firebase when module is imported
firebase_app = init_firebase()
