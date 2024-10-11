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
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\sobre_nosotros.py",
    title="About Me",
    icon="🖤",
    default=True,
)
project_1_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\dashboard_ventas.py",
    title="Sales Dashboard",
    icon="🖤",
)
project_2_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\chatbot.py",
    title="Chat Bot",
    icon="🖤",
)
