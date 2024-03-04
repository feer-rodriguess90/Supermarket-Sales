# Import Libraries Streamlit build Dashboard - Pandas data manipulation - Plotly Build Charts
import streamlit as st
import pandas as pd
import plotly.express as px 

# Setting page size
st.set_page_config(layout="wide")

# Read CSV file
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Add image
# df.add_layout_image(
#     dict(
#         source="https://github.com/feer-rodriguess90/Supermarket-Sales/blob/main/Logo-DataViz.png",
#         xref="paper", yref="paper",
#         x=1, y=1.05,
#         sizex=0.2, sizey=0.2,
#         xanchor="right", yanchor="bottom"
#     )
# )

# Change Date type using to_datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by Date
df = df.sort_values("Date")

# Analyze per months - Concatenate year and month
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Month", df["Month"].unique())

# Create a filter per month
df_filtered = df[df["Month"] == month]

# Create the page layout with streamlit
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Chart Revenue Filter per Day, Subsidiary, Unit
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Revenue Per Day")
col1.plotly_chart(fig_date)

# Chart Filter Product Type
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Revenue By Product Type",      orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Chart Evaluation Per Branch
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Revenue By Branch")
col3.plotly_chart(fig_city, use_container_width=True)

# Chart Revenue By Payment methods
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Revenue By Payment Methods")
col4.plotly_chart(fig_kind, use_container_width=True)

# Chart Average Rating By City
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Evaluation")
col5.plotly_chart(fig_rating, use_container_width=True)