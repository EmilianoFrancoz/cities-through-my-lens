import streamlit as st
import base64
import textwrap
import pandas as pd
import plotly.express as px


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


/* Título principal */

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


[data-testid="stMetricLabel"] {{
    justify-content: center;
}}


[data-testid="stMetricValue"] {{
    text-align: center;
}}


[data-testid="stMetric"] > div {{
    text-align: center;
}}


/* ---------------- EXPLORE THE JOURNEY ---------------- */

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
    margin-bottom: 20px !important;
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


with col1:
    st.metric(
        label="📷 Fotografías",
        value="50"
    )


with col2:
    st.metric(
        label="📍 Lugares",
        value="4"
    )


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


# ============================================================
# DATOS DE LOS LUGARES
# ============================================================

places = pd.DataFrame({
    "Lugar": [
        "New York",
        "Connecticut",
        "Madrid",
        "La Paz"
    ],

    "Fotografías": [
        15,
        12,
        12,
        11
    ],

    "Latitud": [
        40.7128,
        41.6032,
        40.4168,
        -16.4897
    ],

    "Longitud": [
        -74.0060,
        -73.0877,
        -3.7038,
        -68.1193
    ]
})


# ============================================================
# MAPA INTERACTIVO
# ============================================================

fig = px.scatter_geo(
    places,

    lat="Latitud",
    lon="Longitud",

    hover_name="Lugar",

    hover_data={
        "Fotografías": True,
        "Latitud": False,
        "Longitud": False
    },

    size="Fotografías",

    projection="natural earth"
)


# ============================================================
# DISEÑO DEL MAPA
# ============================================================

fig.update_geos(

    showland=True,
    landcolor="#1b222b",

    showocean=True,
    oceancolor="#0e1117",

    showcountries=True,
    countrycolor="#3a424c",

    showcoastlines=True,
    coastlinecolor="#4b5563",

    bgcolor="#0e1117"
)


fig.update_traces(

    marker=dict(
        line=dict(
            width=1,
            color="white"
        )
    )
)


fig.update_layout(

    height=520,

    margin=dict(
        l=0,
        r=0,
        t=10,
        b=0
    ),

    paper_bgcolor="#0e1117",
    plot_bgcolor="#0e1117",

    font=dict(
        color="white"
    )
)


# ============================================================
# MOSTRAR MAPA
# ============================================================

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)
