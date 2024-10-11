# sobre_nosotros.

import streamlit as st

def main():
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\foto_perfil_linkedin.jpg", width=230)

    with col2:
        st.title("Arnaldo Quiñones", anchor=False)
        st.write("Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial, específicamente como oficial de negocios retail. Durante mi tiempo en administración, adquirí habilidades significativas en la preparación de informes utilizando SQL, contribuyendo así a la eficiencia operativa y la toma de decisiones informadas.")
        
if __name__ == "__main__":
    main()
