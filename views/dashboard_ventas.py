# Importo librerias.
import streamlit as st

# CSS para cambiar el color de fondo y de todo el texto
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #00008B);
}

h1, h2, body, p {
    color: #FFFFFF;  /* Cambia el color del texto para todo el contenido */
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\pag_en_construccion.png", width=690)
