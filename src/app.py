import streamlit as st
import sidebar as sb
import tabbar as tb
import os

os.environ['DISPLAY'] = ':0'

st.set_page_config(
    page_title="PyWhatApp",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded")

sb.sidebar()

st.write("# Welcome to PyWhatApp! 👋")
st.text("🚀 Power up your WhatsApp messaging with bulk send and quick send in one simple tool.") 
#st.markdown("""✨ **100% Free** • 🔒 **Privacy First** • 🚫 **No Data Stored or Shared** • 🙌 **No Login, No Signup** — Just open and send your messages! We respect your privacy and never collect, store, or share any information you enter in the app.""")
tb.tabbar()
print(os.environ['DISPLAY'])