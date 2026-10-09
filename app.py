
import streamlit as st
import base64
from pathlib import Path

import pandas as pd
import plotly.express as px


# ============================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Cities Through My Lens",
    page_icon="📷",
    layout="wide"
)


# ============================================================
# 2. RUTAS DE LAS FOTOGRAFÍAS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

HERO_IMAGE = BASE_DIR / "DSC_0081.jpeg"

PHOTO_FOLDERS = {
    "La Paz, BCS": BASE_DIR / "photos" / "la_paz",
    "New York": BASE_DIR / "photos" / "new_york",
    "Connecticut": BASE_DIR / "photos" / "connecticut",
    "Madrid": BASE_DIR / "photos" / "madrid"
}

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp"
}


def get_base64_image(image_path):
    if image_path.is_file():
        return base64.b64encode(
            image_path.read_bytes()
        ).decode("utf-8")
    return None


def get_photos(folder_path):
    if not folder_path.is_dir():
        return []

    return sorted(
        [
            file
            for file in folder_path.iterdir()
            if file.is_file()
            and file.suffix.lower() in IMAGE_EXTENSIONS
        ],
        key=lambda file: file.name.lower()
    )


hero_image = get_base64_image(HERO_IMAGE)


# ============================================================
# 3. ESTILOS CSS
# ============================================================

st.markdown(
    """
<style>

.hero {
    height: 420px;
    border-radius: 18px;
    background-size: cover;
    background-position: center 55%;
    display: flex;
    align-items: center;
    padding: 0 60px;
    margin-bottom: 25px;
    box-sizing: border-box;
}

.hero-content {
    max-width: 650px;
}

.hero-title {
    color: white !important;
    font-size: 58px !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    letter-spacing: -1px;
    margin: 0 !important;
}

.hero-subtitle {
    color: rgba(255,255,255,0.88) !important;
    font-size: 18px !important;
    line-height: 1.5 !important;
    margin-top: 18px !important;
    margin-bottom: 0 !important;
}

[data-testid="stMetric"] {
    background-color: #161b22;
    border: 1px solid #2a3038;
    border-radius: 14px;
    padding: 22px 24px;
    min-height: 125px;
}

[data-testid="stMetricLabel"] {
    justify-content: center;
}

[data-testid="stMetricValue"] {
    text-align: center;
}

[data-testid="stMetric"] > div {
    text-align: center;
}

.section-title {
    color: white !important;
    font-size: 34px !important;
    font-weight: 700 !important;
    margin-top: 50px !important;
    margin-bottom: 5px !important;
}

.section-subtitle {
    color: #a9b1ba !important;
    font-size: 16px !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
}

.insight-box {
    background-color: #161b22;
    border: 1px solid #2a3038;
    border-left: 5px solid #00BFFF;
    border-radius: 14px;
    padding: 24px 28px;
    margin-top: 15px;
    margin-bottom: 40px;
}

.insight-title {
    color: white !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    margin: 0 0 8px 0 !important;
}

.insight-text {
    color: #a9b1ba !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    margin: 0 !important;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# 4. PORTADA
# ============================================================

if hero_image:

    st.markdown(
        f"""
<style>
.hero {{
    background-image:
        linear-gradient(
            90deg,
            rgba(0,0,0,0.78) 0%,
            rgba(0,0,0,0.45) 45%,
            rgba(0,0,0,0.05) 100%
        ),
        url("data:image/jpeg;base64,{hero_image}");
}}
</style>
""",
        unsafe_allow_html=True
    )

    hero_html = (
        '<div class="hero">'
        '<div class="hero-content">'
        '<h1 class="hero-title">'
        'CITIES<br>THROUGH MY LENS'
        '</h1>'
        '<p class="hero-subtitle">'
        "A visual journey through the places I've photographed."
        '</p>'
        '</div>'
        '</div>'
    )

    st.markdown(
        hero_html,
        unsafe_allow_html=True
    )

else:

    st.title("CITIES THROUGH MY LENS")

    st.write(
        "A visual journey through the places I've photographed."
    )


# ============================================================
# 5. DATOS DE LOS LUGARES
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

    "País": [
        "United States",
        "United States",
        "Spain",
        "Mexico"
    ],

    "Latitud": [
        40.7128,
        41.6032,
        40.4168,
        24.1426
    ],

    "Longitud": [
        -74.0060,
        -73.0877,
        -3.7038,
        -110.3128
    ]
})


place_colors = {

    "New York": "#00BFFF",

    "Connecticut": "#2ECC71",

    "Madrid": "#FF9F43",

    "La Paz, BCS": "#FF4FA3"
}


# ============================================================
# 6. MÉTRICAS PRINCIPALES
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        label="📷 Fotografías",
        value=int(places["Fotografías"].sum())
    )


with col2:
    st.metric(
        label="📍 Lugares",
        value=len(places)
    )


with col3:
    st.metric(
        label="🌎 Países",
        value=places["País"].nunique()
    )


# ============================================================
# 7. EXPLORE THE JOURNEY
# ============================================================

st.markdown(
    '<h2 class="section-title">Explore the Journey</h2>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="section-subtitle">Discover the places behind the photographs.</p>',
    unsafe_allow_html=True
)


# ============================================================
# 8. MAPA INTERACTIVO
# ============================================================

map_fig = px.scatter_geo(

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

    size_max=25,

    projection="natural earth"
)


map_fig.update_geos(

    showland=True,
    landcolor="#2F6B6D",

    showocean=True,
    oceancolor="#101C2C",

    showlakes=True,
    lakecolor="#173A5E",

    showcountries=True,
    countrycolor="#A9C5C7",

    showcoastlines=True,
    coastlinecolor="#D1E3E4",

    bgcolor="#0E1117"
)


map_fig.update_traces(

    marker=dict(

        opacity=0.95,

        line=dict(
            width=2,
            color="white"
        )
    )
)


map_fig.update_layout(

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


st.plotly_chart(

    map_fig,

    use_container_width=True,

    config={
        "displayModeBar": False
    }
)


# ============================================================
# 9. WHERE DID I PHOTOGRAPH?
# ============================================================

st.markdown(
    '<h2 class="section-title">Where Did I Photograph?</h2>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="section-subtitle">Comparing the number of photographs captured in each place.</p>',
    unsafe_allow_html=True
)


places_chart = places[
    ["Lugar", "Fotografías"]
].copy()


places_chart["Porcentaje"] = (
    places_chart["Fotografías"]
    / places_chart["Fotografías"].sum()
    * 100
)


places_chart["Etiqueta"] = (
    places_chart["Fotografías"].astype(str)
    + " photos · "
    + places_chart["Porcentaje"].round().astype(int).astype(str)
    + "%"
)


# ============================================================
# 10. GRÁFICA POR LUGAR
# ============================================================

places_fig = px.bar(

    places_chart,

    x="Fotografías",

    y="Lugar",

    color="Lugar",

    color_discrete_map=place_colors,

    text="Etiqueta",

    orientation="h",

    custom_data=["Porcentaje"]
)


places_fig.update_traces(

    textposition="outside",

    cliponaxis=False,

    marker=dict(
        line=dict(
            width=1,
            color="rgba(255,255,255,0.4)"
        )
    ),

    hovertemplate=(
        "<b>%{y}</b><br>"
        "Photographs: %{x}<br>"
        "Percentage: %{customdata[0]:.0f}%"
        "<extra></extra>"
    )
)


places_fig.update_yaxes(

    categoryorder="array",

    categoryarray=[
        "La Paz, BCS",
        "Madrid",
        "Connecticut",
        "New York"
    ],

    title=None,

    tickfont=dict(
        color="white",
        size=14
    ),

    showgrid=False
)


places_fig.update_xaxes(

    title="Number of photographs",

    range=[0, 19],

    showgrid=True,

    gridcolor="rgba(255,255,255,0.08)",

    zeroline=False,

    dtick=5,

    tickfont=dict(
        color="#a9b1ba"
    ),

    title_font=dict(
        color="#a9b1ba"
    )
)


places_fig.update_layout(

    height=470,

    margin=dict(
        l=20,
        r=100,
        t=20,
        b=50
    ),

    paper_bgcolor="#0E1117",

    plot_bgcolor="#0E1117",

    font=dict(
        color="white"
    ),

    showlegend=False,

    bargap=0.30
)


st.plotly_chart(

    places_fig,

    use_container_width=True,

    config={
        "displayModeBar": False
    }
)


# ============================================================
# 11. STORYTELLING / INSIGHT
# ============================================================

insight_html = (
    '<div class="insight-box">'
    '<p class="insight-title">'
    '📍 New York leads the journey.'
    '</p>'
    '<p class="insight-text">'
    'With 15 photographs, New York represents 30% '
    'of the collection, making it the most photographed '
    'place in this visual journey.'
    '</p>'
    '</div>'
)

st.markdown(
    insight_html,
    unsafe_allow_html=True
)


# ============================================================
# 12. EXPLORE THE PHOTOGRAPHY
# ============================================================

st.markdown(
    '<h2 class="section-title">Explore the Photography</h2>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="section-subtitle">Discover the stories and photographs behind each destination.</p>',
    unsafe_allow_html=True
)


# ============================================================
# 13. SELECTOR DE DESTINOS
# ============================================================

selected_place = st.selectbox(

    "Choose a destination",

    options=[
        "La Paz, BCS",
        "New York",
        "Connecticut",
        "Madrid"
    ],

    index=0
)


# ============================================================
# 14. DESCRIPCIONES DE LOS DESTINOS
# ============================================================

destination_descriptions = {

    "La Paz, BCS": (
        "A photographic journey through La Paz, "
        "Baja California Sur, Mexico."
    ),

    "New York": (
        "Exploring the streets and architecture "
        "of New York."
    ),

    "Connecticut": (
        "Discovering the landscapes and atmosphere "
        "of Connecticut."
    ),

    "Madrid": (
        "A visual exploration of Madrid, Spain."
    )
}


st.subheader(selected_place)

st.caption(
    destination_descriptions[selected_place]
)


# ============================================================
# 15. CARGAR FOTOGRAFÍAS AUTOMÁTICAMENTE
# ============================================================

selected_folder = PHOTO_FOLDERS[selected_place]

photos = get_photos(selected_folder)


# ============================================================
# 16. GALERÍA FOTOGRÁFICA DE DOS COLUMNAS
# ============================================================

if photos:

    st.write(
        f"📷 {len(photos)} photographs in this collection"
    )

    col_left, col_right = st.columns(
        2,
        gap="medium"
    )

    for index, photo in enumerate(photos):

        selected_column = (
            col_left
            if index % 2 == 0
            else col_right
        )

        with selected_column:

            st.image(
                str(photo),
                use_container_width=True
            )

            st.caption(
                f"Photograph {index + 1:02d}"
            )

else:

    st.info(
        "This destination's photo gallery "
        "is coming soon."
    )


# ============================================================
# 17. PIE DE PÁGINA
# ============================================================

st.divider()

st.caption(
    "Cities Through My Lens · "
    "Photography & Visual Storytelling"
)
