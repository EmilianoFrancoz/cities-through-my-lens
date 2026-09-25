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
        "La Paz, BCS"
    ],

    "Fotografías": [
        15,
        12,
        12,
        11
    ],

    "Latitud": [
        40.7128,     # New York
        41.6032,     # Connecticut
        40.4168,     # Madrid
        24.1426      # La Paz, Baja California Sur
    ],

    "Longitud": [
        -74.0060,    # New York
        -73.0877,    # Connecticut
        -3.7038,     # Madrid
        -110.3128    # La Paz, Baja California Sur
    ]
})


# ============================================================
# COLORES DE LOS LUGARES
# ============================================================

place_colors = {

    "New York": "#00BFFF",

    "Connecticut": "#2ECC71",

    "Madrid": "#FF9F43",

    "La Paz, BCS": "#FF4FA3"
}


# ============================================================
# MAPA INTERACTIVO
# ============================================================

fig = px.scatter_geo(

    places,

    lat="Latitud",
    lon="Longitud",

    color="Lugar",

    color_discrete_map=place_colors,

    hover_name="Lugar",

    hover_data={
        "Fotografías": True,
        "Latitud": False,
        "Longitud": False
    },

    size="Fotografías",

    size_max=24,

    projection="natural earth"
)


# ============================================================
# ESTILO DEL MAPA
# ============================================================

fig.update_geos(

    showland=True,
    landcolor="#202833",

    showocean=True,
    oceancolor="#0E1117",

    showlakes=True,
    lakecolor="#111827",

    showcountries=True,
    countrycolor="#59636F",

    showcoastlines=True,
    coastlinecolor="#687482",

    bgcolor="#0E1117"
)


# ============================================================
# ESTILO DE LOS PUNTOS
# ============================================================

fig.update_traces(

    marker=dict(

        line=dict(
            width=1.5,
            color="white"
        ),

        opacity=0.9
    )
)


# ============================================================
# DISEÑO GENERAL DEL MAPA
# ============================================================

fig.update_layout(

    height=540,

    margin=dict(
        l=0,
        r=0,
        t=20,
        b=10
    ),

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    font=dict(
        color="white"
    ),

    legend=dict(

        title="Places",

        orientation="h",

        yanchor="bottom",
        y=0.01,

        xanchor="center",
        x=0.5,

        bgcolor="rgba(14,17,23,0.75)"
    )
)


# ============================================================
# PERSONALIZAR HOVER
# ============================================================

fig.update_traces(

    hovertemplate=
        "<b>%{hovertext}</b><br>"
        "Photographs: %{marker.size}"
        "<extra></extra>"
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
