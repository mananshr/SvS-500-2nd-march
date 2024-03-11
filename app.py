import pandas as pd
import streamlit as st
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# import plotly.express as px

st.set_page_config(
    page_title="DMN Data Central"
)

df = pd.read_csv("./data.csv")

st.title(":red[__SvS__] Data 500 :sunglasses:", anchor="head", help="State 500 vs 497")

# print(df)

st.session_state.state = "500"
st.session_state.alliance = "DMN"
st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Enable comparator mode", key="disabled")
    st.radio("Select State", key="state", options=["500", "497", "Both"])

with col2:
    alliance = st.selectbox(
        "Please Select an alliance to be compared to DMN",
        df['Alliance'],
        disabled=not st.session_state.disabled
    )
