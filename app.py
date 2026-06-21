import streamlit as st
from chatbot import get_response

# Page Config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.chat-title {
    text-align: center;
    color: #1f77b4;
    font-size: 40px;
    font-weight: bold;
}

.chat-subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}

.stChatMessage {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<p class="chat-title">🤖 AI Chatbot with NLP</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="chat-subtitle">Powered by Gemini + NLTK</p>',
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("📌 Project Info")

    st.info("""
    AI Chatbot Internship Project

    Features:
    - NLP Preprocessing
    - Intent Detection
    - Gemini AI
    - Chat History
    """)

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            reply = get_response(st.session_state.messages)

            st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

chat_history = ""

for msg in st.session_state.messages:

    chat_history += (
        f"{msg['role']}: "
        f"{msg['content']}\n\n"
    )

st.download_button(
    label="📥 Download Chat",
    data=chat_history,
    file_name="chat_history.txt",
    mime="text/plain"
)