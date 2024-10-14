# sobre_nosotros.
import requests
import re
import streamlit as st

# --- POP UP WINDOW ---

WEBHOOK_URL = "https://hooks.pabbly.com/api/webhook/670c56b88df01fec66f88c3f"


# --- Basic regex pattern for email validation ---
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

@st.dialog("Contactame")
def show_contact_form():
    with st.form("contact_form"):
        first_name = st.text_input("Nombre")
        last_name = st.text_input("Apellido")
        email = st.text_input("Email")
        message = st.text_area("Mensaje")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
                if not WEBHOOK_URL:
                    st.error("Email service is not set up. Please try again later.", icon="📧")
                    st.stop()

                if not first_name:
                    st.error("Please provide your name.", icon="🧑")
                    st.stop()

                if not last_name:
                    st.error("Please provide your last name.", icon="🧑")
                    st.stop() 

                if not email:
                    st.error("Please provide your email address.", icon="📨")
                    st.stop()

                if not is_valid_email(email):
                    st.error("Please provide a valid email address.", icon="📧")
                    st.stop()

                if not message:
                    st.error("Please provide a message.", icon="💬")
                    st.stop()

                # Prepare the data payload and send it to the specified webhook URL
                data = {"email": email, "name": first_name, "message": message}
                response = requests.post(WEBHOOK_URL, json=data)

                if response.status_code == 200:
                    st.success("Your message has been sent successfully! 🎉", icon="🚀")
                else:
                    st.error("There was an error sending your message.", icon="😨")
            

# --- PRINCIPAL ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\frente.png", width=230)

with col2:
        st.title("Arnaldo Quiñones", anchor=False)
        st.write("Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial.")
        if st.button("📧 Contactame"):
                show_contact_form()
        
# --- EXPERIENCIA Y CALIFICACIONES ---

st.write("\n")
st.write("\n")
st.write("\n")
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

st.subheader("Hard skills.")
st.write(
      """
- Lenguajes de programación: Experto en Python con más de 12 años de experiencia.

- Herramientas de análisis y visualización: Power BI, Tableau, MicroStrategy, Excel avanzado.

- Gestión de bases de datos y ETL: SQL, MySQL, Google Cloud, Snowflake, Docker.

- Machine Learning y BI: Experiencia en SSAS, SSIS, SSRS, y proyectos de análisis predictivo.
"""
)