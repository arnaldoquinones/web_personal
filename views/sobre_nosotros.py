# sobre_nosotros.

import streamlit as st

@st.dialog("Contactame")
def show_contact_form():
    with st.form("contact_form"):
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        email = st.text_input("Email")
        message = st.text_area("Your message")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.success("Message succesfully sent!   🚀")
            

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