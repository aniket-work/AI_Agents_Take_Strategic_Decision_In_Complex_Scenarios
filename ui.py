import streamlit as st
import asyncio
from main import run_ai_agent
from constants import LOG_FILE

st.title("Reflection AI Agent for Strategic Decisions")

if st.button("Run AI Agent"):
    st.write("Running AI Agent...")
    asyncio.run(run_ai_agent())
    st.write("AI Agent Finished.")

if st.button("Show Log"):
    with open(LOG_FILE, 'r') as file:
        log = file.read()
    st.text_area("Log Output", log, height=400)
