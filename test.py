import pandas as pd

all_teams = dict()

for year in range(2000, 2024):
    df = pd.read_excel(f"fantasy_football\\data\\coaches\\coaches_{year}.xlsx")
    for i, row in df.iterrows():
        team = row["Team"]
        all_teams[team] = year

pd.DataFrame(all_teams.items()).to_excel("teams.xlsx", index=False)
