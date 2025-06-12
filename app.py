# app.py
# Profiling Pegawai AI – RAG + Agentic Early Warning System (Streamlit)
# Colabs: Sopian & Dani

import streamlit as st
from rag_engine import initialize_rag_agent
from visualization import show_heatmap
import pandas as pd
import os

st.set_page_config(page_title="Profiling Pegawai – Early Warning System", layout="wide")
st.sidebar.title("🛡️ Early Warning System SDM")
st.sidebar.markdown("**Kolaborasi:** Sopian & Dani")

st.title("📂 Profiling Pegawai dengan RAG + Agentic AI")
uploaded_file = st.file_uploader("Upload dokumen audit atau laporan HR (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("📚 Memproses dokumen..."):
        file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        agent = initialize_rag_agent(file_path)
        st.success("✅ Agent siap digunakan!")

        st.subheader("💬 Tanya Jawab Dokumen")
        query = st.text_input("Masukkan pertanyaan tentang pegawai atau redflag")
        if query:
            with st.spinner("🧠 Memproses jawaban..."):
                response = agent.run(query)
                st.markdown(f"**Jawaban AI:** {response}")

        st.markdown("---")
        st.subheader("🔥 Heatmap Risiko Pegawai")
        data_path = "data/redflag_output.csv"
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            show_heatmap(df)
        else:
            st.warning("Belum ada data redflag. Harap unggah dan proses dokumen terlebih dahulu.")
else:
    st.info("Silakan unggah dokumen untuk mulai analisis profiling pegawai.")
