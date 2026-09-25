import streamlit as st
import base64

# --------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# --------------------------------

st.set_page_config(
    page_title="Cities Through My Lens",
    page_icon="📷",
    layout="wide"
)


# --------------------------------
# CARGAR IMAGEN
# --------------------------------

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


img = get_base64_image("DSC_0081.jpeg")


# --------------------------------
# DISEÑO HERO
# --------------------------------

st.markdown(
    f"""
    <style>

    /* Contenedor principal de la portada */
    .hero {{
        height: 420px;
        border-radius: 18px;

        background-image:
            linear-gradient(
                90deg,
                rgba(0, 0, 0, 0.78) 0%,
                rgba(0, 0, 0, 0.45) 45%,
                rgba(0, 0, 0, 0.05) 100%
            ),
            url("data:image/jpeg;base64,{img}");

        background-size: cover;
        background-position: center 55%;

        display: flex;
        align-items: center;

        padding: 0 60px;
        margin-bottom: 25px;

        box-sizing: border-box;
    }}


    /* Área donde está el texto */
    .hero-content {{
        max-width: 650px;
    }}


    /* Título principal */
    .hero-title {{
        color: white;
        font-size: 58px;
        font-weight: 700;
        line-height: 1.05;
        letter-spacing: -1px;
        margin: 0;
    }}


    /* Subtítulo */
    .hero-subtitle {{
        color: rgba(255, 255, 255, 0.88);
        font-size: 18px;
        margin-top: 18px;
    }}

    </style>


    <div class="hero">

        <div class="hero-content">

            <h1 class="hero-title">
                CITIES<br>
                THROUGH MY LENS
            </h1>

            <p class="hero-subtitle">
                A visual journey through the places I've photographed.
            </p>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)
