
## PART I
# with open("Projects/day-25-read-csv/weather_data.csv") as file:
#     content = file.readlines()
#     print(content)
# for l in content:
#     print(l.strip("/n"))


## PART II
# import csv
# temperatures_list = []
# with open("Projects/day-25-read-csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         #print(row)
#         if row[1] != "temp":
#             temperatures_list.append(int(row[1]))

# print(temperatures_list)


## PART III
import pandas as pd

df_weather = pd.read_csv("Projects/day-25-read-csv/pandas-intro/weather_data.csv")
# print(df_weather["temp"])
# print(df_weather.to_dict())
# print(df_weather["temp"].to_list())
# print(df_weather["temp"].mean())
# print(df_weather["temp"].max())
# print(df_weather[df_weather["day"]=="Monday"])
# print(df_weather.iloc[df_weather["temp"].idxmax()])
# print(df_weather[df_weather["temp"].max() == df_weather["temp"]])

# GET MONDAY TEMP AND CONVERT TO FAHRENHEIT
# monday_temp = df_weather[df_weather["day"]=="Monday"]["temp"][0]
# monday_temp_f = monday_temp * (9/5) + 32
# print(monday_temp_f)

