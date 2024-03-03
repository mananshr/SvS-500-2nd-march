import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("./data.csv")

st.title(":red[__SvS__] Data 500 :sunglasses:", anchor="head", help="State 500 vs 497")

df

score = df.sum(1, True, True)[0]

# st.write(score)

st.metric("DMN final score", score)

st.metric("DMN Day 1", df.)
