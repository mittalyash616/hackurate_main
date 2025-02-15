# import threading
# import streamlit as st
# import time
# import requests
# import os
# import logging

# from testfile import voice

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Retrieve API key from environment variables
# api_key = os.getenv("GOOGLE_GENAI_API_KEY")

# if not api_key:
#     st.error("GOOGLE_GENAI_API_KEY not found in environment variables. Please set it.")
#     st.stop()

# # Shared lists for communication between threads
# l1 = []
# l2 = []
# user_messages = []
# lock = threading.Lock()
# voice_done = threading.Event()

# def voice_function():
#     try:
#         print("Voice thread started")  # Debugging
#         with lock:
#             voice(l1, l2)
#         print(f"l1: {l1}, l2: {l2}")  # Debugging
#     except Exception as e:
#         logger.error(f"Voice input error: {e}")
#     voice_done.set()
#     print("Voice thread completed")  # Debugging

# def get_gemini_response(prompt, api_key):
#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + api_key
#     headers = {"Content-Type": "application/json"}
#     payload = {
#         "contents": [{"parts": [{"text": prompt}]}]
#     }
#     try:
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()
#         return response.json()["candidates"][0]["content"]["parts"][0]["text"]
#     except requests.exceptions.RequestException as e:
#         logger.error(f"Gemini API Error: {e}")
#         return f"Gemini API Error: {e}"
#     except (KeyError, IndexError, TypeError) as e:
#         logger.error(f"Gemini Response Parsing Error: {e}")
#         return f"Gemini Response Parsing Error: {e}"

# def display_function():
#     if not voice_done.is_set():
#         st.write("Waiting for voice input...")
#         return

#     if l1 and l2:
#         with lock:
#             prompt = l1.pop(0) + l2.pop(0)
#         user_messages.append(f"User: {prompt}")
#         st.session_state.messages = user_messages
#         st.session_state.processing = True
#         try:
#             response = get_gemini_response(prompt, api_key)
#             user_messages.append(f"Gemini: {response}")
#         except Exception as e:
#             logger.error(f"Gemini Processing Error: {e}")
#             user_messages.append(f"Gemini Processing Error: {e}")
#         st.session_state.messages = user_messages
#         st.session_state.processing = False

# def main():
#     st.title("Voice Interaction with Gemini")

#     # Initialize session state
#     if 'messages' not in st.session_state:
#         st.session_state.messages = []
#     if 'processing' not in st.session_state:
#         st.session_state.processing = False

#     # Display previous messages
#     for message in st.session_state.messages:
#         st.text(message)

#     # Start voice thread
#     if st.button("Start Voice Input"):
#         voice_thread = threading.Thread(target=voice_function, daemon=True)
#         voice_thread.start()

#     # Display processing spinner
#     if st.session_state.processing:
#         with st.spinner("Processing..."):
#             time.sleep(1)  # Simulate processing delay

#     # Call display function
#     display_function()

# if __name__ == '__main__':
#     main()