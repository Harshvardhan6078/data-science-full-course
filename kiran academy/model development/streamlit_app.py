# --- IDE Run Interceptor ---
import sys
import os
if os.environ.get("STREAMLIT_IS_RUNNING") != "true":
    import subprocess
    print("Intercepting Play button... launching Streamlit properly.")
    os.environ["STREAMLIT_IS_RUNNING"] = "true"
    subprocess.run(["streamlit", "run", __file__])
    sys.exit(0)

import streamlit as st
import google.generativeai as genai
import os

# --- Page Setup ---
st.set_page_config(page_title="Harshvardhan Chatbot", page_icon="🤖", layout="centered")

# --- UI Header ---
st.title("🤖 Harshvardhan Chatbot")
st.write("A fast, responsive web interface connected to Gemini 2.5 Flash.")

# --- API Configuration ---
# SECURITY WARNING: You should NEVER upload your actual API key to GitHub!
# We set this up to read securely from Streamlit Cloud's "Secrets" vault.
try:
    # This runs when deployed online
    api_key = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    # If running locally, you must set an environment variable or paste your key below (but delete it before deploying!)
    api_key = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")

try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Failed to configure API: {e}")

# --- Initialize Model and Chat Session ---
SYSTEM_INSTRUCTION = """
You are a highly capable, professional, and responsive personal assistant. 
1. Help the user solve day-to-day problems quickly.
2. Be an excellent conversational partner to help the user practice their English communication. 
   - Proactively but politely correct any grammatical errors or awkward phrasing in their English before responding to their question.
   - Suggest better vocabulary where appropriate.
"""

# Check if we already created the chat session in this browser window
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_INSTRUCTION
    )
    st.session_state["chat_session"] = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Render Previous Chat History ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Handle User Input ---
if prompt := st.chat_input("Start typing here..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and stream bot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Send message to the AI
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            
            # Stream it word by word into the website UI
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
                
            # Remove the blinking cursor at the end
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error connecting to AI: {e}")
            full_response = "Sorry, I encountered an error."

    # Save bot response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
