# Importo librerias.
import streamlit as st
import fastapi as fastAPI

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

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\galactica.ico")
st.sidebar.markdown("Made with ❤️ by [Sven](https://youtube.com/@codingisfun)")


# --- RUN NAVIGATION ---
pg.run()