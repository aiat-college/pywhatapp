import streamlit as st

from playwrite_client import send_whatsapp_message

def send_quick_message(phone_numbers, message):
    numbers = [num.strip() for num in phone_numbers.split(",") if num.strip()]
    for num in numbers:
        sendMessage(num, message)
    return True  

def send_bulk_messages(contact_list, phoneCol, nameCol, message, hasName):    
    for _, row in contact_list.iterrows():
        phone_number = row[phoneCol]
        content = message 
        if hasName:
            name = row[nameCol]            
            if isinstance(name, str) and name.strip() != "":
                content = message.replace("%NAME%", name).replace("%name%", name)
        sendMessage(phone_number, content)     
    return True  

def sendMessage(phone_number, message):        
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number.strip()
    
    try:
        send_whatsapp_message(phone_number, message)
        st.toast(f"Message sent to {phone_number}", icon="✅")
        print(f"Message sent to {phone_number}")        
    except Exception as e:
        st.toast(f"Error sending message to {phone_number}: {e}", icon="❌")
        print("message not sent to", phone_number, "due to error:", e)
    return True  