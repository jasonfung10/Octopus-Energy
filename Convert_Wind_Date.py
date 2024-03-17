import requests
import pandas as pd
import os
from datetime import date


os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(r"01_wind.csv")
df.rename(columns={"category":"date"}, inplace=True)
df["date"] = pd.to_datetime(df["date"],format="%d.%m.%Y")
df.rename(columns={"Wind in m/s":"wind_speed"}, inplace=True)

new_date= pd.date_range('20240101',"20240201", freq="30min", inclusive="left")
#print(new_date)
df2 = pd.DataFrame({"DateTime":new_date})

wind = []
for day in df2["DateTime"]:
     for day1 in df["date"]:
        if day.day == day1.day:
            add_wind = df.loc[df["date"]==day1,"wind_speed"].values[0]
            wind.append(add_wind)


df2["wind"]= wind
df2.to_csv("01_wind_formatted.csv")


df_feb = pd.read_csv(r"02_wind.csv")
df_feb.rename(columns={"category":"date"}, inplace=True)
df_feb["date"] = pd.to_datetime(df_feb["date"],format="%d.%m.%Y")
df_feb.rename(columns={"Wind in m/s":"wind_speed"}, inplace=True)

new_date_feb= pd.date_range('20240201',"20240301", freq="30min", inclusive="left")
df2_feb = pd.DataFrame({"DateTime":new_date_feb})

wind_feb = []
for day_feb in df2_feb["DateTime"]:
     for day1_feb in df_feb["date"]:
        if day_feb.day == day1_feb.day:
            add_wind_feb = df_feb.loc[df_feb["date"]==day1_feb,"wind_speed"].values[0]
            wind_feb.append(add_wind_feb)


df2_feb["wind"]= wind_feb
df2_feb.to_csv("02_winf_formatted.csv")
