import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

bike_daily = pd.read_csv("day.csv")
bike_hourly = pd.read_csv("hour.csv")
bike_df = bike_daily.merge(bike_hourly, on="dteday", how="inner", suffixes=("_daily", "_hourly"))

weather = {
    1: "Clear",
    2: "Mist",
    3: "Light Rain",
    4: "Heavy Rain"
}
bike_df["weather"] = bike_df["weathersit_daily"].map(weather)
bike_df.groupby("weather")["cnt_daily"].mean().reset_index()

values = [0]
bike_2012 = bike_daily[bike_daily. yr . isin (values) == False ]
values = [1]
bike_2011 = bike_daily[bike_daily. yr . isin (values) == False ]
bike_2011.groupby("mnth")["cnt"].sum().reset_index()
bike_2012.groupby("mnth")["cnt"].sum().reset_index()

bike_df.groupby('holiday_daily')['cnt_daily'].mean().reset_index()

st.header("Bike Rental Dashboard :sparkles:")

st.subheader("Average of Daily Rental Bikes Based on Weather")

bike_weather = bike_df.groupby("weather")["cnt_daily"].mean().reset_index().sort_values("cnt_daily")
st.metric("Highest Average", value=format(bike_weather.cnt_daily[0], ".2f"))
x = bike_weather.weather
y = bike_weather.cnt_daily
fig, ax = plt.subplots()
ax.barh(x, y, height = 0.5, color = ("#5CC0C0","#5CC0C0","#F1FABF"))
ax.set_xlabel("Average of Rental Bikes")
ax.set_ylabel("Weather")
plt.show()

st.pyplot(fig)

st.subheader("Monthly Rental Bikes 2011-2012")

col1, col2 = st.columns(2)

with col1:
  bike_series1 = bike_2011.groupby("mnth")["cnt"].sum().reset_index()
  st.metric("Highest in 2011", value=bike_series1.cnt[5])
  x = bike_series1.mnth
  y = bike_series1.cnt
  fig, ax = plt.subplots()
  ax.plot(x, y, color = "#5CC0C0", marker='o', markerfacecolor='#2F6790', linestyle='dashed')
  ax.set_xlabel("Month")
  ax.set_ylabel("Monthly Rental Bikes in 2011")
  ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
  ax.set_xticklabels(("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
  plt.show()
  st.pyplot(fig)

with col2:
  bike_series2 = bike_2012.groupby("mnth")["cnt"].sum().reset_index()
  st.metric("Highest in 2012", value=bike_series2.cnt[8])
  x = bike_series2.mnth
  y = bike_series2.cnt
  fig, ax = plt.subplots()
  ax.plot(x, y, color = "#5CC0C0", marker='o', markerfacecolor='#2F6790', linestyle='dashed')
  ax.set_xlabel("Month")
  ax.set_ylabel("Monthly Rental Bikes in 2012")
  ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
  ax.set_xticklabels(("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
  plt.show()
  st.pyplot(fig)

st.subheader("Bike Rental Between Weekday and Weekend")

bike_holiday = bike_df.groupby('holiday_daily')['cnt_daily'].mean().reset_index()
st.metric("Average Rental in Weekdays", value=format(bike_holiday.cnt_daily[0], ".2f"))
x = bike_holiday.holiday_daily
y = bike_holiday.cnt_daily
fig, ax = plt.subplots()
ax.pie(y, labels = ("Weekday","Weekend"), autopct = "%1.1f%%", colors = ["#F1FABF","#5CC0C0"])
plt.show()

st.pyplot(fig)

st.caption("Copyright (c)")