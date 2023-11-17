import fantasy_football.predictor.loader as loader
import pandas as pd
import numpy as np
from xgboost import XGBClassifier


def xgboost_features():
    df_offense = loader.combine_nfl_measure_tables(factor="offense")
    df_offense = df_offense.add_suffix("_offense")
    df_defense = loader.combine_nfl_measure_tables(factor="defense")
    df_defense = df_defense.add_suffix("_defense")
    df = df_offense.merge(
        right=df_defense,
        left_on=["year_offense", "team_id_offense"],
        right_on=["year_defense", "team_id_defense"],
    )
    df = df[df["year_offense"] != 2023]
    df = df.drop(
        [
            "points_per_game_offense",
            "extra_points_made_offense",
            "extra_points_attempted_offense",
            "points_per_game_defense",
            "total_touchdowns_defense",
            "points_against_defense",
            "year_offense",
            "year_defense",
            "team_id_offense",
            "team_id_defense",
            "games_offense",
            "games_defense",
            "made_playoffs_offense",
        ],
        axis=1,
    )
    df = df.rename(columns={"made_playoffs_defense": "made_playoffs"})
    X = df.loc[:, df.columns != "made_playoffs"]
    y = df["made_playoffs"]

    runs = list()
    for i in range(100):
        model = XGBClassifier()
        model.fit(X, y)
        fi = model.feature_importances_
        runs.append(fi)
    run_mean = np.mean(np.array(runs), axis=0)
    return pd.DataFrame(run_mean, index=df.columns[:-1])
