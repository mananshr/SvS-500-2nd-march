import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("./data.csv")

st.title(":red[__SvS__] Data 500 :sunglasses:", anchor="head", help="State 500 vs 497")


