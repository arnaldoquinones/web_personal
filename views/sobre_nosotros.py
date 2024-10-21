# Importo librerias.

import requests
import re
import streamlit as st
import base64
import streamlit as st
import plotly.express as px



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

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #000066; /* Azul más oscuro */
    color: #ffffff; /* Texto blanco */
    border: 1px solid #ffffff; /* Bordes blancos, grosor de 1 píxel */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra para el efecto 3D */
    transition: all 0.3s ease; /* Suaviza el efecto al hacer hover */
}
div.stButton > button:hover {
    background-color: #00004d; /* Un tono aún más oscuro al hacer hover */
    color: #ffffff; /* Texto blanco */
    border: 1px solid #ffffff; /* Bordes blancos en hover */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4); /* Aumenta la sombra al hacer hover para el efecto 3D */
    transform: translateY(-2px); /* Mueve el botón hacia arriba al hacer hover */
}
</style>
""", unsafe_allow_html=True)


# --- POP UP WINDOW ---

WEBHOOK_URL = ("https://hooks.pabbly.com/api/webhook/670c56b88df01fec66f88c3f")


# --- Codigo validacion de mail ---
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def reset_form():
    first_name = ""
    last_name = ""
    email = ""
    message = ""
    st.session_state.form_visible = False

@st.dialog("Contactame")
def show_contact_form():
    with st.form("contact_form",clear_on_submit=True):
        first_name = st.text_input("Nombre")
        last_name = st.text_input("Apellido")
        email = st.text_input("Email")
        message = st.text_area("Mensaje")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if not WEBHOOK_URL:
                st.error("El servicio de correo no está configurado. Por favor, inténtalo de nuevo más tarde.", icon="📧")
                st.stop()

            if not first_name:
                st.error("Por favor, proporciona tu nombre.", icon="🧑")
                st.stop()

            if not last_name:
                st.error("Por favor, proporciona tu apellido.", icon="🧑")
                st.stop() 

            if not email:
                st.error("Por favor, proporciona tu dirección de correo electrónico.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Por favor, proporciona una dirección de correo electrónico válida.", icon="📧")
                st.stop()

            if not message:
                st.error("Por favor, proporciona un mensaje.", icon="💬")
                st.stop()

            # Prepare the data payload and send it to the specified webhook URL
            data = {"email": email, "name": first_name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("¡Tu mensaje se ha enviado correctamente! 🎉", icon="🚀")
                # reset_form()
            else:
                st.error("Hubo un error al enviar tu mensaje.", icon="😨")
                # reset_form()

            # Restablecer los campos
first_name = ""
last_name = ""
email = ""
message = ""
            

# --- PRINCIPAL ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\portada.png", width=230)

with col2:
        st.title("Arnaldo Quiñones", anchor=False)
        st.write("Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial.")
        if st.button("📧 Contactame"):
                show_contact_form()
                reset_form()

        
# --- EXPERIENCIA Y CALIFICACIONES ---

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.subheader("Experiencia y calificaciones.")

st.write(
      """
- Experiencia en análisis de datos financieros: Más de 24 años en el Banco ICBC como Data Analyst, manejando información crítica.

- Formación en Ciencia de Datos y Machine Learning: Ingeniero en Ciencia de Datos con experiencia en herramientas como Python, Snowflake, y Tableau.

- Habilidad en procesos ETL y sistemas: Experto en integración de datos con Docker, Google Cloud y Power BI.

- Experiencia docente y liderazgo: Profesor en la Universidad de Buenos Aires y líder en proyectos corporativos y de digitalización.
"""
)

st.write("\n")
st.markdown(""" 
            
---
            
   """)
st.write("\n")
st.subheader("Hard skills.")
st.write(
      """
- Lenguajes de programación: Experto en Python con más de 12 años de experiencia.

- Herramientas de análisis y visualización: Power BI, Tableau, MicroStrategy, Excel avanzado.

- Gestión de bases de datos y ETL: SQL, MySQL, Google Cloud, Snowflake, Docker.

- Machine Learning y BI: Experiencia en SSAS, SSIS, SSRS, y proyectos de análisis predictivo.
"""
)