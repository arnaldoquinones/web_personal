# Importo librerias.
import streamlit as st
import fastapi as fastAPI

# -- PAGE SETUP --
st.set_page_config(
    page_title="Mi Aplicación",  # Título de la página que debería aparecer en la pestaña del navegador
    page_icon=r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\galactica.ico"  # Ruta completa al ícono
)
# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)