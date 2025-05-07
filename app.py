import streamlit as st
from agent_workflow import handle_query
import time

st.set_page_config(page_title="RAG-Powered Q&A Assistant", page_icon="🤖", layout="centered")
st.markdown("""
<style>
body {font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #1F2937, #3B82F6); color: white;}
.css-1d391kg {background: transparent;}
.answer-box {transition: opacity 0.5s ease-in-out; opacity: 0; margin-top: 10px; padding: 15px; background-color: rgba(255, 255, 255, 0.1); border-radius: 8px;}
.answer-box.show {opacity: 1;}
.question-card {background: rgba(255, 255, 255, 0.15); padding: 12px; border-radius: 8px; margin-bottom: 8px;}
.question-card:hover {background: rgba(255, 255, 255, 0.25);}
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🤖 RAG-Powered Q&A Assistant")
st.markdown(""" 
### Ask any question, and our intelligent assistant will answer using the knowledge base.
""")

# Query History
if "history" not in st.session_state:
    st.session_state.history = []

# Input Area
query = st.text_input("Ask your question here:", placeholder="Type your question...")

# Animated Button
if st.button("Get Answer ✨") and query.strip() != "":
    with st.spinner("Generating answer... Please wait ✨"):
        answer = handle_query(query)
        st.session_state.history.append((query, answer))

        st.markdown("## 💡 Your Answer")

        answer_box = st.empty()
        answer_box.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)

        time.sleep(0.5)  # Short delay for animation to apply

        st.markdown("<script>document.querySelector('.answer-box').classList.add('show');</script>", unsafe_allow_html=True)

        st.success("Answer generated successfully!")

# Displaying Query History
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Query History")
    for q, a in st.session_state.history[-5:][::-1]:
        st.markdown(f"<div class='question-card'><strong>Q:</strong> {q}<br><strong>A:</strong> {a}</div>", unsafe_allow_html=True)
