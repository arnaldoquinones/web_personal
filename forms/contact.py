import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First name")
        last_name = st.text_input("Last name")
        email = st.text_input("Email")
        message = st.text_area("Your message")
        submit_button = st.form_submit_button("Submit")

if submit_button:
    st.success("Message succesfully sent!")

