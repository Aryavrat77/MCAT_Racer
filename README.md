# MCAT QuizRacer

A real-time multiplayer quiz game for MCAT preparation. Race through questions with friends and compete on the leaderboard!

## Features

- Real-time multiplayer quiz sessions
- Live leaderboard
- MCAT-style questions
- Room-based gameplay
- Firebase backend for real-time updates

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up Firebase:
   - Create a Firebase project
   - Download your Firebase service account key as `firebase_key.json`
   - Place it in the project root

## Running Locally

```bash
streamlit run main.py
```

## Deployment

The app is configured for deployment on Streamlit Cloud. Make sure to:
1. Add your Firebase credentials to Streamlit secrets
2. Connect your GitHub repository
3. Deploy!

## Project Structure

- `main.py` - Main application entry point
- `quiz.py` - Quiz session management
- `questions.py` - MCAT questions database
- `firebase.py` - Firebase operations
- `firebase_config.py` - Firebase configuration