import firebase_admin
from firebase_admin import credentials, db
import os
import streamlit as st
import json

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
                # Convert Streamlit secrets to the format Firebase expects
                firebase_creds = {
                    "type": st.secrets.firebase.type,
                    "project_id": st.secrets.firebase.project_id,
                    "private_key_id": st.secrets.firebase.private_key_id,
                    "private_key": st.secrets.firebase.private_key,
                    "client_email": st.secrets.firebase.client_email,
                    "client_id": st.secrets.firebase.client_id,
                    "auth_uri": st.secrets.firebase.auth_uri,
                    "token_uri": st.secrets.firebase.token_uri,
                    "auth_provider_x509_cert_url": st.secrets.firebase.auth_provider_x509_cert_url,
                    "client_x509_cert_url": st.secrets.firebase.client_x509_cert_url
                }
                cred = credentials.Certificate(firebase_creds)
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