import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import numpy as np

df = pd.read_csv("all_data.zip", compression='zip')


def linePlotParam(param, df):
    fig_param = px.line(df, x="Time", y=param, title=param+ ' Trends')
    # fig_power.show()
    fig_param.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig_param)
    return

def multiplePlots(params, df):
    fig = go.Figure()
    Time = np.array(df["Time"])
    for param in params:
        p = np.array(df[param])
        fig.add_trace(go.Scatter(x=Time, y=p,mode='lines',name=param))
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
        xaxis=(dict(showgrid=False))
    )
    
    st.plotly_chart(fig)
    return

if __name__ == "__main__":

    st.set_page_config(page_title="Plots", page_icon=":bar_chart:", layout="wide")

    st.sidebar.header("Please Filter Here:")
    dev_id = st.sidebar.radio(
        "Select the Device:",
        options=df["device_id"].unique(),
        # default=df["device_id"].unique()[0]
    )

    date = st.sidebar.multiselect(
        "Select the Date (Only One):",
        options=df["Date"].unique(),
        default=df["Date"].unique()[0],
    )

    params = st.sidebar.multiselect(
        "Select Parameters:",
        options=["volt", "curr","mc_st", "power", "pf"],
        default=["volt", "curr", "power"]
    )

    df_selection = df.query(
        "device_id == @dev_id & Date ==@date"
    )
    # st.markdown("###")
    # total_power = round(float(df_selection["power"].sum()),2)
    # st.subheader(f"Total Power: {total_power:,}")
    # st.markdown("""---""")
    st.markdown("###")
    st.subheader("Parameters Plots")
    multiplePlots(params, df_selection)
    st.markdown("""---""")
    st.markdown("##")
    st.subheader("Summary of Power Generated")
    st.markdown("> Sum of Power in the day / 24/ 1000")
    df_filter = df[df["device_id"]==dev_id]
    dates = df_filter["Date"].unique()
    power = []
    # print(dates)
    for d in dates:
        pow = (df_filter[df_filter["Date"] == d]["power"].sum() / 1000)/24
        power.append(pow)
    # print(power)

    bar_fig = px.bar(x = dates, y=power)
    st.plotly_chart(bar_fig)
    st.markdown("""---""")
    st.markdown("###")
    st.subheader("Individual Parameter Plots")
    for param in params:
        linePlotParam(param, df_selection)
    st.markdown("""---""")
    




    # ---- HIDE STREAMLIT STYLE ----
    # hide_st_style = """
    #             <style>
    #             #MainMenu {visibility: hidden;}
    #             footer {visibility: hidden;}
    #             header {visibility: hidden;}
    #             </style>
    #             """
    # st.markdown(hide_st_style, unsafe_allow_html=True)
