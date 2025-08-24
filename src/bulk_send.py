import streamlit as st
import pandas as pd
import message_client as mc

def bulk_send():
    st.warning("Use this option to import data from an Excel file. Ensure that your file is properly structured, as you will later be able to select the appropriate columns for names and phone numbers!")

    uploaded_file = st.file_uploader("Choose your Excel file", type=["xlsx", "xls"])

    if uploaded_file:
        try:
            phoneCol = ""
            nameCol = ""

            df = pd.read_excel(uploaded_file)            
            st.text("Preview of the uploaded data. Use this view to identify and select the columns for names and phone numbers.")
            st.dataframe(df.head())  
            
            columns = df.columns.tolist()                
            phoneCol = st.selectbox(
                "Select the phone number column",
                columns,
                help="Select the column from the above sample data that contains the phone numbers to be used for sending messages.",
            )  

            hasName = st.checkbox("Include recipient names in the message", help="When enabled, the message will include each recipient’s name; otherwise, only their phone number will be used.")

            if hasName:
                col1, col2 = st.columns(2)
                with col1:
                    nameCol = st.selectbox(
                        "Select the user name column",
                        columns,
                        help="Select the column from the above sample data that contains the user names to be used for sending messages.",
                    )
                with col2:
                    with st.container(border=True):
                        st.markdown(
                            'Use the placeholder <code style="font-size:1.2em;"><b>@NAME</b></code> in your message to insert the recipient\'s name.',
                            unsafe_allow_html=True
                        )
            
            msg_hint = "Type your message here . . . . . ."
            if hasName:
                msg_hint = "Dear  @NAME,   Greetings from PyWhatApp! . . . . ."
            message = st.text_area("Message:", placeholder=msg_hint, height="content", key="bulk_send_message")

            agree = st.checkbox("I confirm that 'WhatsApp Web' is logged in on this browser.", key="bulk_send_agree")
            if not agree:
                st.warning("To use PyWhatApp, the browser must be logged in to 'WhatsApp Web' (https://web.whatsapp.com/) using the sender’s number. Please complete this step to enable the service.")
                return

            if st.button("Send Message", type="primary", key="btn_send_bulk_message", disabled=st.session_state.get("is_msg_sending", False)):
                if message is None or message.strip() == "":
                    st.error("💬 Your message is empty — type something to send!")
                else:
                    mc.send_bulk_messages(df, phoneCol.strip(), nameCol.strip(), message, hasName)

        except Exception as e:
            st.error(f"Error: {e} \n try again later.")
            return               
        