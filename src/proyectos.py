# Importo librerias.
import streamlit as st


# CSS para cambiar el color de fondo y de todo el texto
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #00008B);
}

h1, h2, h3, h4, h5, h6, p, li, ul, ol, span {
    color: #FFFFFF !important;  /* Cambia el color del texto */
    text-align: justify;  /* Justifica el texto */
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(135deg, #000000, #00008B);  /* Fondo del sidebar */
}

[data-testid="stText"] {
    color: #FFFFFF !important;  /* Cambia el color del texto de cualquier otro componente de texto */
    text-align: justify;  /* Justifica el texto */
}
</style>
"""

# --- RUTAS RELATIVAS ---
pag_en_construccion_path = "./media/pag_en_construccion.png"

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Proyectos.")

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.image(pag_en_construccion_path, width=690)
