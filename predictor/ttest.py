from scipy.stats import ttest_ind
import pandas as pd
import fantasy_football.predictor.loader as loader


def run_ttest_offense():
    df_offense = loader.load_data_offense()
    df_offense = df_offense.drop(["year", "team_id", "games"], axis=1)
    df_playoffs = df_offense[df_offense["made_playoffs"] == True]
    df_playoffs = df_playoffs.drop(["made_playoffs"], axis=1)
    df_not_playoffs = df_offense[df_offense["made_playoffs"] == False]
    df_not_playoffs = df_not_playoffs.drop(["made_playoffs"], axis=1)
    data = list()
    for col in df_playoffs.columns:
        col_data = list()
        col_data.append(col)
        t_stat, p_value = ttest_ind(df_playoffs[col], df_not_playoffs[col])
        col_data.append(t_stat)
        col_data.append(p_value)
        data.append(col_data)
    df = pd.DataFrame(data=data, columns=["Factor", "t-stat", "p-value"])
    df["Significant"] = df["p-value"] < 0.05
    return df


def run_ttest_defense():
    df_defense = loader.load_data_defense()
    df_defense = df_defense.drop(["year", "team_id", "games"], axis=1)
    df_playoffs = df_defense[df_defense["made_playoffs"] == True]
    df_playoffs = df_playoffs.drop(["made_playoffs"], axis=1)
    df_not_playoffs = df_defense[df_defense["made_playoffs"] == False]
    df_not_playoffs = df_not_playoffs.drop(["made_playoffs"], axis=1)
    data = list()
    for col in df_playoffs.columns:
        col_data = list()
        col_data.append(col)
        t_stat, p_value = ttest_ind(df_playoffs[col], df_not_playoffs[col])
        col_data.append(t_stat)
        col_data.append(p_value)
        data.append(col_data)
    df = pd.DataFrame(data=data, columns=["Factor", "t-stat", "p-value"])
    df["Significant"] = df["p-value"] < 0.05
    return df
