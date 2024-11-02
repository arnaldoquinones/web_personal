# Importo librerias.
import streamlit as st
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

pagina_principal_path = "pagina_principal.py"
resumen_curricular_path = "resumen_curricular.py"
chatbot_path = "chatbot.py"
proyectos_path = "proyectos.py"
logo_path = "../media/menu.png"


pagina_principal = st.Page(
    pagina_principal_path,
    title="Pagina principal.",
    icon="🌟",
)

resumen_curricular = st.Page(
    resumen_curricular_path,
    title="Resumen curricular.",
    icon="🌟",
)

proyectos = st.Page(
    proyectos_path,
    title="Proyectos.",
    icon="🌟",
)

chatbot = st.Page(
    chatbot_path,
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
st.logo(logo_path)
st.sidebar.markdown('Made by&nbsp;<a href="https://github.com/arnaldoquinones" target="_blank">Arnaldo Quiñones.</a>', unsafe_allow_html=True)



# --- RUN NAVIGATION ---
pg.run()