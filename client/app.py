import sys
from pathlib import Path

# Añade el directorio raíz al path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

import streamlit as st
from client.components.upload import render_uploader
from client.components.chatUI import render_chat
from client.components.history_download import render_history_download



st.set_page_config(
    page_title="RAGBot Streamlit",
    layout="wide",
)
st.title("RAGBot Streamlit")

render_uploader()
render_chat()
render_history_download()