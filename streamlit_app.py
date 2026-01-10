import streamlit as st
import requests
import google.auth.transport.requests
from google.oauth2 import service_account
import google.auth

PROJECT_ID = "customersupportbot-anwb"
SESSION_ID = "123456"

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)


# ---------------- DIALOGFLOW CALL ----------------
def detect_intent(text: str) -> str:
    url = (
        f"https://dialogflow.googleapis.com/v2/projects/"
        f"{PROJECT_ID}/agent/sessions/{SESSION_ID}:detectIntent"
    )

    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)

    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json",
    }

    data = {
        "queryInput": {
            "text": {
                "text": text,
                "languageCode": "en",
            }
        }
    }

    response = requests.post(url, headers=headers, json=data, timeout=15)
    response.raise_for_status()
    return response.json()["queryResult"]["fulfillmentText"]

# ---------------- UI ----------------
st.set_page_config(page_title="Customer Support Chatbot", layout="centered")
st.title("🤖 Customer Support Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello 👋 How can I help you today? "
                       "You can ask about login, refund, delivery, or complaints."
        }
    ]

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_text = st.chat_input("Type your message...")

if user_text:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Get bot reply
    try:
        bot_reply = detect_intent(user_text)
    except Exception as e:
        bot_reply = "Sorry, something went wrong. Please try again."

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # (Optional) Limit history length

    st.session_state.messages = st.session_state.messages[-30:]
