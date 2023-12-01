import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
import time


# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')
    return pd.read_csv(r"us_state_vaccinations.csv")

data = load_data()

# Set Title
st.title("Streamlit Test")

# Visualization 1
st.subheader('Map with Layers')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Number of Map Layers", "2", "200%")

st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] {
   color: rgb(232, 0, 0);
}
</style>
""", unsafe_allow_html=True)
# fig, ax = plt.subplots()
# data.plot(ax=ax)
# st.pyplot(fig)
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[600, 900, 700, 800]',
            # get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

# Create two columns for the layout
col1, col2 = st.columns(2)

# Visualization 2 in the left column
with col1:
    st.subheader('Geospatial Data Visualization')
    # st.button("Refresh Data", type="primary")
    if st.button('Refresh Data'):
        data = load_data()
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    st.pyplot(fig)

# Drill-down feature in the right column
with col2:
    st.subheader('Location Details')
    selected_country = st.selectbox('Select a State', data['location'].unique())
    st.write(data[data['location'] == selected_country])