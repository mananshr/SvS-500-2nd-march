import pandas as pd
import streamlit as st

import plotly.express as px

# import numpy as np
# from PIL import Image

st.set_page_config(
    page_title="DMN Data Central"
)

# def flip_diagonal(df):
#     rows, cols = df.shape
#     flipped_df = pd.DataFrame(np.zeros((cols, rows)), columns=df.columns, index=df.index)
#     for i in range(rows):
#         for j in range(cols):
#             flipped_df.iloc[j, i] = df.iloc[i, j]
#     return flipped_df


df = pd.read_csv("./data.csv")
dmn_data = df[df["Alliance"]=="DMN"]
st.title(":red[__SvS__] Data 500 :sunglasses:", anchor="head", help="State 500 vs 497")

if "state" not in st.session_state:
    st.session_state.state = 500
    st.session_state.disabled = False
    st.session_state.alliance = 'BOM'

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
    alliance_list = df[df["State"] == st.session_state.state]
    # print(alliance_list)
    alliance_list = alliance_list["Alliance"]
    if st.session_state.state == 500:
        alliance_list = alliance_list.drop(0)
    option = st.selectbox(
        "Compare Your Alliance with DMN",
        alliance_list,
        # index=1,
        disabled=not st.session_state.disabled,
    )
    st.session_state.alliance = option

if st.session_state.disabled:

    compared_state = dmn_data._append(df[df["Alliance"] == st.session_state.alliance])
    # compared_state
    st.bar_chart(compared_state, x="Alliance", y=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

    # compared_state_pivot = compared_state.pivot("Day 1", "Day 2", "Day 3", "Day 4", "Day 5")
    # compared_state_pivot = compared_state
    # compared_state.pivot(index="Alliance", values=[compared_state_pivot = compared_state.pivot("Day 1", "Day 2", "Day 3", "Day 4", "Day 5")])
    # compared_state_pivot
    # compared_state
    # st.line_chart(compared_state, x=["Day 1", "Day 2","Day 3", "Day 4","Day 5"], y="Alliance")

    compared_state_temp = compared_state.rename(columns={'Day 6': 'Battle Day'})
    compared_state_temp = compared_state_temp.drop("State", axis=1)
    # compared_state_pivot = compared_state_temp.pivot(index="Alliance", columns="Alliance")
    # compared_state_pivot = pd.pivot_table(compared_state_temp, values=)
    # compared_state_pivot = flip_diagonal(compared_state_temp)
    st.dataframe(compared_state_temp, hide_index=True)

    compared_state_temp = compared_state_temp.drop("Battle Day", axis=1)
    compared_state_temp = compared_state_temp.drop("Alliance", axis=1)
    # sum_df = pd.DataFrame(columns=["Sum"])
    compared_state_temp = compared_state_temp.sum(axis=1)
    # compared_state_temp.columns = ["Sum"]
    # compared_state_temp
    sum_vals = pd.Series(compared_state_temp)
    # sum_vals
    sum_names = compared_state["Alliance"].squeeze()
    # sum_names
    sums_df = pd.concat([sum_names, sum_vals,], axis=1)
    # sums_df.rename(columns={0: "Prep days total"})
    sums_df.columns.values[1] = "Prep Days Total"
    # sums_df

    st.subheader("Day 1")
    fig = px.pie(compared_state, values="Day 1", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.subheader("Day 2")
    fig = px.pie(compared_state, values="Day 2", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.subheader("Day 3")
    fig = px.pie(compared_state, values="Day 3", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.subheader("Day 4")
    fig = px.pie(compared_state, values="Day 4", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.subheader("Day 5")
    fig = px.pie(compared_state, values="Day 5", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.header("Prep Days Total Score")
    fig = px.pie(sums_df, values='Prep Days Total', names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    st.header("Battle Day")
    fig = px.pie(compared_state, values="Day 6", names="Alliance", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

else:
    state_df = df[df["State"]==st.session_state.state]
    state_df = state_df.drop("State", axis=1)
    st.header("Prep days")
    st.bar_chart(state_df, x="Alliance", y=["Day 1", "Day 2","Day 3", "Day 4","Day 5"])

    st.subheader("Day 1")
    fig = px.pie(state_df, values="Day 1", names="Alliance")
    st.plotly_chart(fig)

    st.subheader("Day 2")
    fig = px.pie(state_df, values="Day 2", names="Alliance")
    st.plotly_chart(fig)

    st.subheader("Day 3")
    fig = px.pie(state_df, values="Day 3", names="Alliance")
    st.plotly_chart(fig)

    st.subheader("Day 4")
    fig = px.pie(state_df, values="Day 4", names="Alliance")
    st.plotly_chart(fig)

    st.subheader("Day 5")
    fig = px.pie(state_df, values="Day 5", names="Alliance")
    st.plotly_chart(fig)

    st.header("Battle Day")
    fig = px.pie(state_df, values="Day 6", names="Alliance")
    st.plotly_chart(fig)

