import streamlit as st

@st.dialog("Terms and Conditions", width="large")
def tnc_dialog():
    st.markdown("""

        Please read these Terms and Conditions (“Terms”) before using **PyWhatApp**. By accessing or using our application, you agree to these Terms.

        ### 1. Purpose of the App
        - This app is designed to help users send WhatsApp messages in bulk or individually using the pywhatkit library.
        - It is for lawful, personal, or business communication purposes only.

        ### 2. User Responsibilities
        - You are responsible for ensuring you comply with WhatsApp’s own **Terms of Service**.
        - You must not use this app to send spam, unsolicited messages, or content that violates laws or WhatsApp policies.
        - You are solely responsible for the accuracy of the data you enter (phone numbers, messages, etc.).

        ### 3. No Data Storage
        - The app does not collect, store, or share any personal data. All processing happens locally on your device.

        ### 4. Disclaimer of Liability
        - The developer is **not responsible** for:
            - Any data loss, damage, or breach that occurs while using the app.
            - Misuse of the app by the user.
            - Any limitations, errors, or failures in the pywhatkit library or WhatsApp Web.

        ### 5. No Warranty
        - The app is provided **“as is”** without any warranties of any kind.
        - We do not guarantee uninterrupted or error-free operation.

        ### 6. Changes to the Terms
        - We may revise these Terms at any time, with updates posted here and effective immediately upon posting.

        ### 7. Contact Information
        - For any questions or concerns regarding these Terms, please contact us at tech@aiat.edu.in.
    """)


@st.dialog("Privacy Policy", width="large")
def pp_dialog():
    st.markdown("""
        This Privacy Policy explains how **PyWhatApp** (“we,” “our,” or “us”) handles your data when you use our web application.

        ### 1. Data Collection
        - We do **not** collect, store, or share any personal data entered into the app.
        - All data (such as phone numbers, messages, and uploaded Excel files) is processed **locally** in your browser and/or through the underlying **pywhatkit** Python library.

        ### 2. Data Usage
        - Your phone numbers and messages are used **only** to send WhatsApp messages as per your request.
        - No data is transmitted to our servers or any third-party storage.

        ### 3. Third-Party Services
        - This application uses the **pywhatkit** library ([https://pypi.org/project/pywhatkit/](https://pypi.org/project/pywhatkit/)) to interact with WhatsApp Web for sending messages.
        - pywhatkit operates under its own terms and privacy practices, and we do not control or take responsibility for their services.

        ### 4. Data Security
        - Since no data is stored on our side, the risk of a server-side data breach is eliminated.
        - However, users are responsible for ensuring their own device and internet connection are secure.

        ### 5. Disclaimer
        - We are **not responsible** for any data loss, data breach, or misuse of the application by the user.
        - Use of this app is at your own risk.

        ### 6. Changes to This Policy
        - We may update this Privacy Policy at any time. Updates will be posted here with the new effective date.
       
    """)