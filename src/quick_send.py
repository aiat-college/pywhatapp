import streamlit as st
import message_client as mc

def quick_send():
    st.warning("Enter the phone number and your message to send instantly. Ideal for personal or one-off messages. You can also send to multiple recipients by entering phone numbers separated by commas!")

    phone_numbers = st.text_input("Phone number (with country code):", placeholder="e.g., +1234567890, +1987654321", help="Enter one or more phone numbers separated by commas."  )
    message = st.text_area("Message:", placeholder="Type your message here . . . . .", height="content", key="quick_send_message")

    agree = st.checkbox("I confirm that 'WhatsApp Web' is logged in on this browser.", key="quick_send_agree")
    if not agree:
        st.warning("To use PyWhatApp, the browser must be logged in to 'WhatsApp Web' (https://web.whatsapp.com/) using the sender’s number. Please complete this step to enable the service.")
        return
    if st.button("Send Message", type="primary", key="btn_send_quick_message", disabled=st.session_state.get("is_msg_sending", False)):
        if phone_numbers and message:
            mc.send_quick_message(phone_numbers, message)
        elif phone_numbers is None or phone_numbers.strip() == "":
            st.error("📱 Oops! That phone number doesn’t look right. Use digits only, or separate multiple numbers with commas!")
        elif message is None or message.strip() == "":
            st.error("💬 Your message is empty — type something to send!")

