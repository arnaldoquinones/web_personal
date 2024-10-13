import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        message = st.text_area("Your message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
                st.success("Message succesfully sent!🚀")
                st.experimental_rerun()

