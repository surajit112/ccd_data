import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("all_data.zip", compression='zip')

st.set_page_config(page_title="Plots", page_icon=":bar_chart:", layout="wide")

st.sidebar.header("Please Filter Here:")
dev_id = st.sidebar.multiselect(
    "Select the Device:",
    options=df["device_id"].unique(),
    default=df["device_id"].unique()[0]
)

date = st.sidebar.multiselect(
    "Select the Date:",
    options=df["Date"].unique(),
    default=df["Date"].unique()[0],
)


df_selection = df.query(
    "device_id == @dev_id & Date ==@date"
)

# ---- MAINPAGE ----
# st.title(":Plots")
st.markdown("##")

# TOP KPI's
total_power = round(float(df_selection["power"].sum()),2)


# st.subheader("Total Power:")
st.subheader(f"Total Power: {total_power:,}")


st.markdown("""---""")

fig_power = px.line(df_selection, x="Time", y="power", title='Power Trends')
# fig_power.show()
fig_power.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_power)

fig_volt = px.line(df_selection, x="Time", y="volt", title='Volt Trends')
# fig_power.show()
fig_volt.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_volt)

fig_curr = px.line(df_selection, x="Time", y="curr", title='Curr Trends')
# fig_power.show()
fig_curr.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_curr)

fig_pf = px.line(df_selection, x="Time", y="pf", title='pf Trends')
# fig_power.show()
fig_pf.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_pf)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
