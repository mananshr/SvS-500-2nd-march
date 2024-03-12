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
dmn_data = df[df["Alliance"]=="DMN"]
st.title(":red[__SvS__] Data 500 :sunglasses:", anchor="head", help="State 500 vs 497")

if "state" not in st.session_state:
    st.session_state.state = 500
    st.session_state.disabled = False
    st.session_state.alliance = 'DMN'

col1, col2 = st.columns(2)
alliance_list = df["Alliance"]

with col1:
    st.checkbox("Compartor mode", key="disabled")
    print(st.session_state.disabled)
    st.radio(
        "Select State 👉",
        key="state",
        options=set(df["State"])
    )

with col2:
    alliance_list = df[df["State"]==st.session_state.state]
    # print(alliance_list)
    alliance_list=alliance_list["Alliance"]
    option = st.selectbox(
        "Compare Your Alliance with DMN",
        alliance_list,
        disabled=not st.session_state.disabled,
    )
    st.session_state.alliance = option

if st.session_state.disabled:
    print(st.session_state.alliance)
    compared_state = dmn_data._append(df[df["Alliance"]==st.session_state.alliance])
    # compared_state
    st.area_chart(compared_state, x="Alliance", y=["Day 1", "Day 2","Day 3", "Day 4","Day 5"])


state_df = df[df["State"]==st.session_state.state]
state_df = state_df.drop("State", axis=1)
print(state_df)
st.header("Prep days")
st.line_chart(state_df, x="Alliance", y=["Day 1", "Day 2","Day 3", "Day 4","Day 5"])

