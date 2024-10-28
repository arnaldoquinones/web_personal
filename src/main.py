# Importo librerias.
import streamlit as st
import os
# import fastapi as fastAPI
# from forms.contact import contact_form

# --- PAGE FEATURE ---

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# --- PAGE SETUP ---

base_path = "."  # Define tu directorio base

pagina_principal = st.Page(
    os.path.join(base_path, "pagina_principal.py"),
    title="Pagina principal.",
    icon="🌟",
)

resumen_curricular = st.Page(
    os.path.join(base_path, "resumen_curricular.py"),
    title="Resumen curricular.",
    icon="🌟",
)

proyectos = st.Page(
    os.path.join(base_path, "proyectos.py"),
    title="Proyectos.",
    icon="🌟",
)

chatbot = st.Page(
    os.path.join(base_path, "chatbot.py"),
    title="Chat Bot.",
    icon="🌟",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        
        "": [pagina_principal,resumen_curricular, proyectos, chatbot],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\menu.png")
st.sidebar.markdown('Made by&nbsp;<a href="https://github.com/arnaldoquinones" target="_blank">Arnaldo Quiñones.</a>', unsafe_allow_html=True)



# --- RUN NAVIGATION ---
pg.run()