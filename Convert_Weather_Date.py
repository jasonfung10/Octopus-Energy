import requests
import pandas as pd
import os
from datetime import date


os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(r"01_temp.csv")
df.rename(columns={"category":"date"}, inplace=True)
df["mean"] = (df["minimum"]+df["maximum"])/2
df["date"] = pd.to_datetime(df["date"],format="%d.%m.%Y")

#print(df.dtypes)
#print (df)

# today= pd.to_datetime("01/01/2024")
# temp1 = df.loc[df["date"]==today, "mean"].values[0]
# print (df)
# print (temp1)

new_date= pd.date_range('20240101',"20240201", freq="30min", inclusive="left")
#print(new_date)
df2 = pd.DataFrame({"DateTime":new_date})

temp = []
for day in df2["DateTime"]:
     for day1 in df["date"]:
        if day.day == day1.day:
            add_temp = df.loc[df["date"]==day1,"mean"].values[0]
            temp.append(add_temp)


df2["temp"]= temp
df2.to_csv("01_temp_formatted.csv")


df_feb = pd.read_csv(r"02_temp.csv")
df_feb.rename(columns={"category":"date"}, inplace=True)
df_feb["mean"] = (df_feb["minimum"]+df_feb["maximum"])/2
df_feb["date"] = pd.to_datetime(df_feb["date"],format="%d.%m.%Y")

new_date_feb= pd.date_range('20240201',"20240301", freq="30min", inclusive="left")
#print(new_date)
df2_feb = pd.DataFrame({"DateTime":new_date_feb})

temp_feb = []
for day_feb in df2_feb["DateTime"]:
     for day1_feb in df_feb["date"]:
        if day_feb.day == day1_feb.day:
            add_temp_feb = df_feb.loc[df_feb["date"]==day1_feb,"mean"].values[0]
            temp_feb.append(add_temp_feb)


df2_feb["temp"]= temp_feb
df2_feb.to_csv("02_temp_formatted.csv")
