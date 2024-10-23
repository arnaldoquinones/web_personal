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

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.markdown("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium nunc et dui dignissim, at faucibus lacus efficitur. Fusce vulputate, libero a tincidunt finibus, erat felis ullamcorper magna, a lobortis nunc quam at arcu. Ut fermentum nunc non viverra hendrerit. Aliquam erat volutpat. Sed gravida eros nec odio auctor, sit amet faucibus mauris varius. Nulla facilisi. Phasellus vitae justo nec magna scelerisque condimentum.

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium nunc et dui dignissim, at faucibus lacus efficitur. Fusce vulputate, libero a tincidunt finibus, erat felis ullamcorper magna, a lobortis nunc quam at arcu. Ut fermentum nunc non viverra hendrerit. Aliquam erat volutpat. Sed gravida eros nec odio auctor, sit amet faucibus mauris varius. Nulla facilisi. Phasellus vitae justo nec magna scelerisque condimentum. """)
# st.image(r"D:\Users\Arnaldo\Desktop\SISTEMAS\practicas\practicas_apis\FASTAPI\proyecto\images\pag_en_construccion.png", width=690)