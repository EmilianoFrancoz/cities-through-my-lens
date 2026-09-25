import streamlit as st
import base64
import textwrap


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Cities Through My Lens",
    page_icon="📷",
    layout="wide"
)


# ============================================================
# CARGAR LA IMAGEN DE PORTADA
# ============================================================

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


img = get_base64_image("DSC_0081.jpeg")


# ============================================================
# ESTILOS DE LA PÁGINA
# ============================================================

st.markdown(
    f"""
<style>

/* ---------------- HERO ---------------- */

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


/* Contenido del Hero */

.hero-content {{
    max-width: 650px;
}}


/* Título */

.hero-title {{
    color: white !important;

    font-size: 58px !important;
    font-weight: 700 !important;

    line-height: 1.05 !important;
    letter-spacing: -1px;

    margin: 0 !important;
}}


/* Subtítulo */

.hero-subtitle {{
    color: rgba(255, 255, 255, 0.88) !important;

    font-size: 18px !important;

    margin-top: 18px !important;
}}


/* ---------------- MÉTRICAS ---------------- */

[data-testid="stMetric"] {{
    background-color: #161b22;

    border: 1px solid #2a3038;
    border-radius: 14px;

    padding: 22px 24px;

    min-height: 125px;
}}


/* Centrar nombre */

[data-testid="stMetricLabel"] {{
    justify-content: center;
}}


/* Centrar número */

[data-testid="stMetricValue"] {{
    text-align: center;
}}


/* Centrar contenido */

[data-testid="stMetric"] > div {{
    text-align: center;
}}


/* ---------------- SECCIÓN JOURNEY ---------------- */

.journey-title {{
    color: white !important;

    font-size: 34px !important;
    font-weight: 700 !important;

    margin-top: 50px !important;
    margin-bottom: 5px !important;
}}


.journey-subtitle {{
    color: #a9b1ba !important;

    font-size: 16px !important;

    margin-top: 0 !important;
    margin-bottom: 25px !important;
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO / PORTADA
# ============================================================

hero_html = """
<div class="hero"><div class="hero-content"><h1 class="hero-title">CITIES<br>THROUGH MY LENS</h1><p class="hero-subtitle">A visual journey through the places I've photographed.</p></div></div>
"""

st.markdown(
    textwrap.dedent(hero_html),
    unsafe_allow_html=True
)


# ============================================================
# MÉTRICAS PRINCIPALES
# ============================================================

col1, col2, col3 = st.columns(3)


# 50 FOTOGRAFÍAS

with col1:
    st.metric(
        label="📷 Fotografías",
        value="50"
    )


# 4 LUGARES

with col2:
    st.metric(
        label="📍 Lugares",
        value="4"
    )


# 4 CATEGORÍAS

with col3:
    st.metric(
        label="🖼️ Categorías",
        value="4"
    )


# ============================================================
# EXPLORE THE JOURNEY
# ============================================================

journey_html = """
<h2 class="journey-title">Explore the Journey</h2>
<p class="journey-subtitle">Discover the places behind the photographs.</p>
"""

st.markdown(
    textwrap.dedent(journey_html),
    unsafe_allow_html=True
)
