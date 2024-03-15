import pandas as pd
import streamlit as st

import plotly.express as px

st.set_page_config(
    page_title="DMN Data Central"
)

df = pd.read_csv("./data.csv")
df_500_transposed = pd.read_csv("./500_transposed.csv")
df_497_transposed = pd.read_csv("./497_transposed.csv")
dmn_data = df[df["Alliance"] == "DMN"]
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
    alliance_list = alliance_list["Alliance"]
    if st.session_state.state == 500:
        alliance_list = alliance_list.drop(0)
    option = st.selectbox(
        "Compare Your Alliance with DMN",
        alliance_list,
        disabled=not st.session_state.disabled,
    )
    st.session_state.alliance = option

if st.session_state.disabled:

    compared_state = dmn_data._append(df[df["Alliance"] == st.session_state.alliance])
    st.bar_chart(compared_state, x="Alliance", y=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])
    compared_state_sum = compared_state.rename(columns={'Day 6': 'Battle Day'})
    compared_state_sum = compared_state_sum.drop("State", axis=1)

    compared_state_sum = compared_state_sum.drop("Battle Day", axis=1)
    compared_state_sum = compared_state_sum.drop("Alliance", axis=1)
    compared_state_sum = compared_state_sum.sum(axis=1)
    sum_vals = pd.Series(compared_state_sum)
    sum_names = compared_state["Alliance"].squeeze()
    sums_df = pd.concat([sum_names, sum_vals], axis=1)
    sums_df.columns.values[1] = str("Prep Days Total")

    compared_state_temp = compared_state.drop(columns="State")
    compared_state_temp = compared_state_temp.drop(columns="Alliance")
    alliance_list_temp = compared_state.get("Alliance")
    # compared_state_transposed = pd.DataFrame(columns=alliance_list_temp)
    # compared_state_transposed.name = str("Days")
    # alliance_list_temp
    compared_state_transposed = pd.DataFrame()
    compared_state_transposed = compared_state_transposed._append(compared_state_temp.transpose(), ignore_index=True)
    compared_state_transposed.columns = alliance_list_temp
    # compared_state_transposed.index = pd.Index(name="Day-wise Comparison")
    # compared_state_transposed.index = pd.Index.set_names(compared_state_transposed, names='Day-wise Comparison')
    # compared_state_transposed.index = pd.Index(compared_state_temp.get("Alliance"), name="Day-wise Comparison")
    # compared_state_transposed.columns.values[0] = compared_state_temp.iat[0, 0]
    # compared_state_transposed.columns.values[0] = str("DMN")
    # compared_state_transposed
    # st.bar_chart(compared_state_transposed, x="Alliance", y=[0,1])

    compared_state_transposed = compared_state_transposed.assign(Days=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Battle Day"])
    # compared_state_transposed

    st.subheader("Day-wise contribution")
    # fig = px.histogram(compared_state_transposed, x="Days", y=alliance_list_temp)
    # st.plotly_chart(fig)
    st.bar_chart(compared_state_transposed, x="Days", y=alliance_list_temp)

    st.subheader("Day-wise contribution percentage")
    fig = px.histogram(compared_state_transposed, x="Days", y=alliance_list_temp, barnorm="percent")
    st.plotly_chart(fig)

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
    state_df = df[df["State"] == st.session_state.state]
    state_df = state_df.drop("State", axis=1)
    st.header("Prep days")
    st.bar_chart(state_df, x="Alliance", y=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])
    alliance_list = df[df["State"] == st.session_state.state]
    alliance_list = alliance_list["Alliance"]
    df_transposed = pd.DataFrame

    if st.session_state.state == 500:
        df_transposed = df_500_transposed
    else:
        df_transposed = df_497_transposed

    st.subheader("Day-wise data")
    st.bar_chart(df_transposed, x="Alliance", y=alliance_list)

    st.subheader("Day-wise contribution percentage")
    fig = px.histogram(df_transposed, x="Alliance", y=alliance_list, barnorm="percent")
    st.plotly_chart(fig)

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

    state_df_temp = state_df.drop(columns="Alliance")
    state_df_temp = state_df_temp.sum(axis=1)
    sum_vals = pd.Series(state_df_temp)
    sum_names = state_df["Alliance"].squeeze()
    sums_df = pd.concat([sum_names, sum_vals], axis=1)
    sums_df.columns.values[1] = "Prep Days Total"

    st.header("Prep Days Total Score")
    fig = px.pie(sums_df, values='Prep Days Total', names="Alliance")
    st.plotly_chart(fig)

    st.header("Battle Day")
    fig = px.pie(state_df, values="Day 6", names="Alliance")
    st.plotly_chart(fig)
