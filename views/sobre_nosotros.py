# sobre_nosotros.py

import streamlit as st
from forms.contact import contact_form  # Importa el formulario desde contact.py

# --- PRINCIPAL ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\frente.png", width=230)

with col2:
    st.title("Arnaldo Quiñones", anchor=False)
    st.write("Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial.")
    if st.button("📧 Contactame"):
        contact_form()  # Llama a la función del formulario que está en contact.py

# --- EXPERIENCIA Y CALIFICACIONES ---
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
