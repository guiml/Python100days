# Create fur color count

import pandas as pd
df_squirrels = pd.read_csv("Projects/day-25-read-csv/squirrel-count/Squirrel_Data.csv")
#print(df_squirrels)


# print(df_squirrels.columns)
grouped_df = df_squirrels.groupby(['Primary Fur Color'])['Primary Fur Color'].count().copy()
print(grouped_df)
