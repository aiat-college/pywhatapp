import streamlit as st
import pywhatkit as kit
import pandas as pd

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
        kit.sendwhatmsg_instantly(phone_no=phone_number, message=message, wait_time=8, tab_close=True, close_time=1)
        st.toast(f"Message sent to {phone_number}", icon="✅")
        print(f"Message sent to {phone_number}")        
    except Exception as e:
        st.toast(f"Error sending message to {phone_number}: {e}", icon="❌")
        print("message not sent to", phone_number, "due to error:", e)
    return True  