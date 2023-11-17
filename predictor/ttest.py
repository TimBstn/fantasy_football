from scipy.stats import ttest_ind
import pandas as pd
import fantasy_football.predictor.loader as loader


def calculate_nfl_playoffs_significance(
    factor: str = "offense", alpha: float = 0.05
) -> pd.DataFrame:
    """
    This function calculates t-statistics and p-values to evaluate the significance
    of a specific NFL measure in predicting whether a team makes the playoffs or not.
    The result DataFrame includes 'Significant' column, indicating significance based
    on the alpha level = 0.05.

    Parameters
    ----------
    factor: str, optional
        The factor to consider, either 'offense' or 'defense'
    alpha: float, optional
        significance level

    Returns
    --------
    pd.DataFrame:
        t-stat: float
            t-statistics
        p-value: float
            p-value of specific measure
        Significant: bool
            measure is significant based on alpha level

    Example
    -------
    >>> import pandas as pd
    >>> result_df = calculate_nfl_playoffs_significance(factor='defensive', alpha=0.05)
    """
    df = loader.combine_nfl_measure_tables(factor=factor)
    df = df.drop(["year", "team_id", "games"], axis=1)
    df_playoffs = df[df["made_playoffs"] == True]
    df_playoffs = df_playoffs.drop(["made_playoffs"], axis=1)
    df_not_playoffs = df[df["made_playoffs"] == False]
    df_not_playoffs = df_not_playoffs.drop(["made_playoffs"], axis=1)
    data = list()
    for col in df_playoffs.columns:
        col_data = list()
        col_data.append(col)
        t_stat, p_value = ttest_ind(df_playoffs[col], df_not_playoffs[col])
        col_data.append(t_stat)
        col_data.append(p_value)
        data.append(col_data)
    df_final = pd.DataFrame(data=data, columns=["Factor", "t-stat", "p-value"])
    df_final["Significant"] = df_final["p-value"] < alpha
    return df_final
