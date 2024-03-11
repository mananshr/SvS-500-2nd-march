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

print(df)

if "state" not in st.session_state:
    st.session_state.state = 500
    st.session_state.disabled = False

col1, col2 = st.columns(2)
alliance_list = df["Alliance"]

with col1:
    st.checkbox("Compartor mode", key="disabled")
    st.radio(
        "Select State 👉",
        key="state",
        options=set(df["State"])
    )

with col2:
    alliance_list = df[df["State"]==st.session_state.state]
    print(alliance_list)
    alliance_list=alliance_list["Alliance"]
    option = st.selectbox(
        "Compare Your Alliance with DMN",
        alliance_list,
        disabled=not st.session_state.disabled,
    )

print()
