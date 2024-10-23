# Importo librerias.
import streamlit as st
# import fastapi as fastAPI
# from forms.contact import contact_form


# --- PAGE SETUP ---
pag_principal = st.Page(
r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\src\pag_principal.py",
    title="Pagina principal.",
    icon="🌟",
    default=True,
)
skills = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\src\skills.py",
    title="Resumen curricular.",
    icon="🌟",
    
)
proyectos = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\src\proyectos.py",
    title="Proyectos.",
    icon="🌟",
)
chatbot = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\src\chatbot.py",
    title="Chat Bot.",
    icon="🌟",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        
        "": [pag_principal,skills, proyectos, chatbot],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\menu.png")
st.sidebar.markdown('Made by&nbsp;<a href="https://github.com/arnaldoquinones" target="_blank">Arnaldo Quiñones.</a>', unsafe_allow_html=True)



# --- RUN NAVIGATION ---
pg.run()