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


df

day_1_val=df['Day 1'].loc[df.index[0]]
day_2_val=df['Day 2'].loc[df.index[0]]
day_3_val=df['Day 3'].loc[df.index[0]]
day_4_val=df['Day 4'].loc[df.index[0]]
day_5_val=df['Day 5'].loc[df.index[0]]

score = df.sum(1, True, True)[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("DMN final score", score)

with col2:
    st.metric("DMN Day 1 Score", day_1_val)

with col3:
    st.metric('DMN Day 2 Score', day_2_val)

# col1, col2, col3 = st.columns(3)

with col1:
    st.metric("DMN Day 3 score", day_3_val)

with col2:
    st.metric("DMN Day 4 Score", day_4_val)

with col3:
    st.metric('DMN Day 5 Score', day_5_val)

with col1:
    st.metric("DMN Day 1 Rank", 1)

with col2:
    st.metric("DMN Day 2 Rank", 1)

with col3:
    st.metric('DMN Day 3 Rank', 1)

with col1:
    st.metric("DMN Day 4 Rank", 1)

with col2:
    st.metric("DMN Day 5 Rank", 1)

with col3:
    st.metric('DMN Battle day rank', 2)

