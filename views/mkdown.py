import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #00008B);
}
[data-testid="stText"] {
    color: #FFFFFF !important;  /* Cambia el color del texto de cualquier otro componente de texto */
    text-align: justify;  /* Justifica el texto */
}
[data-testid="stText"] {
    color: #FFFFFF !important;  /* Cambia el color del texto de cualquier otro componente de texto */
    text-align: justify;  /* Justifica el texto */
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("¡Es verano!")

st.markdown("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium nunc et dui dignissim, at faucibus lacus efficitur. Fusce vulputate, libero a tincidunt finibus, erat felis ullamcorper magna, a lobortis nunc quam at arcu. Ut fermentum nunc non viverra hendrerit. Aliquam erat volutpat. Sed gravida eros nec odio auctor, sit amet faucibus mauris varius. Nulla facilisi. Phasellus vitae justo nec magna scelerisque condimentum.

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pretium nunc et dui dignissim, at faucibus lacus efficitur. Fusce vulputate, libero a tincidunt finibus, erat felis ullamcorper magna, a lobortis nunc quam at arcu. Ut fermentum nunc non viverra hendrerit. Aliquam erat volutpat. Sed gravida eros nec odio auctor, sit amet faucibus mauris varius. Nulla facilisi. Phasellus vitae justo nec magna scelerisque condimentum. """)

