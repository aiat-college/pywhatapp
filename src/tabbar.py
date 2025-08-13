import streamlit as st
import bulk_send as bs
import quick_send as qs

def tabbar():
    tab1, tab2 = st.tabs(["Bulk Send", "Quick Send"])
    with tab1:
        bs.bulk_send()
    with tab2:
        qs.quick_send()


        
    #st.markdown("---")
