# type: ignore

import pandas as pd

data = pd.read_csv("C:\\Users\\ghvw\\projects\\datasets\\Marvel_Comics.csv")

# print(data.head())

# data = data.query('"penciler" == "Jack Kirby"')


# statistics
# print(data.describe())


# rows
# iloc for indexing
# loc for using strings as indexes etc
# print(data.iloc[9])
# print(data.iloc[2:9])

data = data.set_index(data["penciler"])

# print(data.loc["Jack Kirby"])

# filtering?
#print(data[data["penciler"] == "Jack Kirby"].sample())

print(data[(data["penciler"] == "Jack Kirby") &
      (data["comic_name"].str.contains("Captain"))].head())
