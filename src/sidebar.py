import  streamlit as st
import tnc_pp_dialog as tp

def sidebar():
    st.sidebar.info(
        """
        # 💻 PyWhatApp
        **PyWhatApp** is a Python-powered web app 🐍 that lets you send bulk WhatsApp messages 💬📢 effortlessly.  

        ### Key Features
        - ⭐️  **100% Free**  
        - 🔐  **Privacy First**  
        - 🚫  **No Data Stored or Shared**  
        - 🙌  **No Login, No Signup**  
        ---
        Just open and send your messages! We respect your privacy and never collect, store, or share any information you enter in the app.
        """
    )
    st.sidebar.subheader("Get Started")
    import textwrap
    st.sidebar.markdown(textwrap.dedent("""
        1. **Log in to WhatsApp Web** on this browser using the sender’s number at [https://web.whatsapp.com/](https://web.whatsapp.com/).  
        2. **Choose your sending method**:  
            - **Bulk Send** – Upload an Excel file containing recipient details and send messages to all listed users.  
            - **Quick Send** – Enter one or more comma-separated WhatsApp numbers in the format `+country_code phone_number` (e.g., `+1234567890, +1987654321`).  
        3. **Type your message** in the text box. 
        4. **Click 'Send Message'** to deliver your message instantly.  
        5. **Enjoy the convenience** of sending personalized WhatsApp messages quickly and effortlessly!
    """))
    st.sidebar.markdown("---")
    st.sidebar.subheader("Support Us")
    st.sidebar.markdown("""
    If you find PyWhatApp useful, consider supporting us:
    - ⭐️ Star us on [GitHub](https://github.com/aiat-college/pywhatapp)
    """)

    if st.sidebar.button("Terms and Conditions", type="secondary", width="stretch"):
        tp.tnc_dialog()
    if st.sidebar.button("Privacy policy", type="secondary", width="stretch"):
        tp.pp_dialog()

    #st.sidebar.caption("Checkout the source code at [Github](https://github.com/aiat-college/pywhatapp)")
    st.sidebar.markdown("---")  
    st.sidebar.warning("Made with ❤️ by the Team [Auroville Institute of Applied Technology](https://aiat.edu.in/)")
    