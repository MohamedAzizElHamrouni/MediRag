import streamlit as st
import os
from modules.agent import MedicalAgent

st.set_page_config(page_title="Medical Agentic Assistant", page_icon="🧬", layout="wide")

if "agent" not in st.session_state:
    st.session_state.agent = MedicalAgent()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🧬 Medical Agentic Research Assistant")
st.sidebar.header("📂 Gestion des Documents")

uploaded_file = st.sidebar.file_uploader("Charger un PDF médical", type="pdf")
if uploaded_file:
    path = os.path.join("data/medical_pdfs", uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    with st.sidebar:
        with st.spinner("Indexation..."):
            res = st.session_state.agent.rag.ingest_pdf(path)
            st.success(res)

st.sidebar.divider()
if st.sidebar.button("🗑️ Effacer l'historique"):
    st.session_state.chat_history = []
    st.session_state.agent.memory.clear()
    st.rerun()

# Affichage du chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Posez votre question médicale..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("L'agent réfléchit..."):
            response = st.session_state.agent.run(prompt)
            st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
