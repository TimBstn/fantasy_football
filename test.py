import pandas as pd

df = pd.read_excel("lb_2023.xlsx")
print(df.value_counts(subset=["Week"]).sort_index())
