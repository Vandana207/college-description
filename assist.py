import streamlit as st

st.set_page_config(page_title="AITAM Assistant", page_icon="🎓", layout="centered")

# Header
col1, col2 = st.columns([1,4])

with col1:
    st.image("aitam_logo.png", width=90)

with col2:
    st.title("AITAM College Assistant")
    st.write("Ask anything about AITAM College")

st.divider()

# Campus Image
st.image("campus.png", use_container_width=True)

st.divider()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask about timetable, library, departments...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple AI responses
    if "timetable" in prompt.lower():
        reply = "📅 Today's timetable: DS, DBMS, Computer Networks"

    elif "library" in prompt.lower():
        reply = "📚 AITAM library is located in Block G and open from 9 AM to 5 PM."

    elif "principal" in prompt.lower():
        reply = "👨‍🏫 Please visit the administration office for principal details."

    elif "departments" in prompt.lower():
        reply = "🏫 Departments: CSE, ECE, EEE, Mechanical, Civil."

    else:
        reply = "🤖 I am still learning. Please ask about timetable, library, or departments."

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})