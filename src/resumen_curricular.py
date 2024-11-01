# Chatbot.py

import streamlit as st

# CSS para cambiar el color de fondo y de todo el texto.

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #00008B);
}

h1, h2, h3, h4, h5, h6, p, li, ul, ol, span {
    color: #FFFFFF !important;  /* Cambia el color del texto */
    text-align: justify;  /* Justifica el texto */
}

[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(135deg, #000000, #00008B);  /* Fondo del sidebar */
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}               

[data-testid="stText"] {
    color: #FFFFFF !important;  /* Cambia el color del texto de cualquier otro componente de texto */
    text-align: justify;  /* Justifica el texto */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Ambitos de estudio.")

# st.write("\n")
# st.write("\n")
# st.write("\n")
# st.write("\n")

# st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\d_scientist.png", width=690)

# st.write("\n")
# st.write("\n")
# st.write("\n")
# st.write("\n")

# st.subheader("Data Engineering.")


# st.write(
#       """Cuento con una sólida trayectoria en Data Engineering, respaldada por más de 24 años de experiencia en el sector bancario y un enfoque técnico orientado al análisis de datos y la optimización de procesos. A lo largo de mi carrera, he trabajado extensamente en la implementación de pipelines de datos, modelos de machine learning y soluciones de Business Intelligence, aplicando técnicas avanzadas de ETL, SQL, y herramientas como MySQL, Google Cloud, Docker, y Git. Mi experiencia incluye proyectos clave en los que he sido responsable de la ingesta, tratamiento y modelado de grandes volúmenes de datos, garantizando la integridad y eficiencia del flujo de datos en entornos productivos. He utilizado Snowflake y MicroStrategy para transformar datos en información valiosa, facilitando la toma de decisiones estratégicas en empresas del ámbito financiero. Mi enfoque en la automatización de procesos y la escalabilidad de soluciones ha contribuido a la mejora de la operativa de datos, impactando de manera positiva en los resultados de negocio.

# """
# )
# st.write("\n")
# st.markdown(""" 
            
# ---
            
#    """)
# st.write("\n")
# st.subheader("Data Science.")
# st.write(
#       """
# A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.

# Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción. He utilizado herramientas como Python, Google Cloud, MySQL y Power BI, además de frameworks como Snowflake y Docker, para diseñar pipelines de datos eficientes que permiten obtener insights valiosos y transformar datos crudos en información accionable.

# En mi experiencia más reciente, he liderado proyectos de análisis de datos en sectores como el financiero, en donde implementé soluciones de predicción de riesgos y optimización de procesos de negocio. En un proyecto de marketing para la colocación de restaurantes en Estados Unidos, desempeñé un papel clave en la construcción de modelos predictivos que ayudaron a identificar las mejores ubicaciones basadas en variables geográficas, demográficas y de consumo. Mi enfoque en la minería de datos y el análisis exploratorio me ha permitido desarrollar estrategias basadas en datos para resolver problemas complejos de negocio.

# Además de mis habilidades técnicas, también he colaborado en proyectos de BI y análisis estadístico, utilizando herramientas como Tableau y MicroStrategy, lo que me ha permitido comunicar insights de manera clara y efectiva a partes interesadas no técnicas. Mi experiencia en el manejo de grandes volúmenes de datos y mi capacidad para resolver problemas de manera analítica me han permitido adaptarme a desafíos dinámicos, trabajando en equipo y asegurando que los proyectos se completen con éxito.
# """
# )
# st.write("\n")
# st.markdown(""" 
            
# ---
            
#    """)
# st.write("\n")
# st.subheader("Data Analysis.")
# st.write(
#       """
# A lo largo de mi carrera, he trabajado con grandes volúmenes de datos, utilizando herramientas como MySQL, Excel avanzado, Power BI, y Tableau para transformar datos en información útil y accionable.

# Mi principal fortaleza en el análisis de datos es mi capacidad para identificar patrones, tendencias y oportunidades a partir de conjuntos de datos complejos. Durante mi paso por el sector financiero, lideré iniciativas que mejoraron la eficiencia operativa y permitieron la optimización de procesos mediante reportes analíticos basados en datos. En particular, he trabajado en la creación de dashboards interactivos y reportes financieros utilizando herramientas de BI como MicroStrategy y Power BI, brindando insights clave a nivel directivo y comercial.

# En uno de mis proyectos más recientes, participé en el análisis de datos para un estudio de mercado sobre la colocación de restaurantes en Estados Unidos, donde utilicé modelos estadísticos para proporcionar recomendaciones que optimizaron la ubicación y el rendimiento de los establecimientos. Mi habilidad para integrar fuentes de datos dispares y aplicar técnicas de visualización me ha permitido comunicar resultados de manera clara y efectiva a diferentes audiencias, tanto técnicas como no técnicas.

# Además de mi habilidad técnica, me considero una persona analítica, meticulosa y orientada a resultados, capaz de traducir necesidades empresariales en soluciones basadas en datos. Mi experiencia en la limpieza y transformación de datos, junto con mi capacidad para trabajar de manera colaborativa en equipos multidisciplinarios, ha sido clave en el éxito de los proyectos en los que he participado. Estoy siempre dispuesto a aprender nuevas tecnologías y metodologías para seguir aplicando análisis de datos avanzados que generen valor tangible para las organizaciones.
#     """
# )
# st.write("\n")
# st.write("\n")
# st.write("\n")
# st.write("\n")

st.subheader("Data Engineering.")
col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\engineer.png", width=330)

with col2:
        st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning.
""")
st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. 
""")

st.markdown(""" 
            
---
            
   """)
st.write("\n")
st.subheader("Data Science.")
col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:
        st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning.
""")
st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. 
""")
        

with col2:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\scientist.png", width=330)

st.markdown(""" 
            
---
            
   """)
st.subheader("Data Analyst.")
col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\web_personal\media\analyst.png", width=330)

with col2:
        st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning.
""")
st.write("""A lo largo de mi carrera, he trabajado en el desarrollo de modelos predictivos, análisis de datos y proyectos complejos de machine learning, aplicando soluciones que han generado un impacto directo en la toma de decisiones estratégicas y operativas.
Mi enfoque principal ha sido la creación de modelos avanzados de machine learning, desde la fase de ingesta y tratamiento de datos hasta la evaluación y la implementación en entornos de producción altamente cambiantes y demandantes. 
""")