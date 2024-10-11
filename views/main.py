# Importo librerias.
import streamlit as st
import fastapi as fastAPI



# --- PAGE SETUP ---
main_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\main_page.py",
    title="Main.",
    icon="❤️",
    default=True,
)
about_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\sobre_nosotros.py",
    title="Quienes somos.",
    icon="❤️",
    
)
project_1_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\dashboard_ventas.py",
    title="Dashboard de ventas.",
    icon="❤️",
)
project_2_page = st.Page(
    r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\chatbot.py",
    title="Chat Bot.",
    icon="❤️",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [main_page],
        "Projects": [project_1_page, project_2_page,about_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\galactica.ico")
st.sidebar.markdown("Made with ❤️ by [Arnaldo](https://youtube.com/@codingisfun)")


# --- RUN NAVIGATION ---
pg.run()