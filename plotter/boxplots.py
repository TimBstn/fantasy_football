import fantasy_football.predictor.loader as loader
import matplotlib.pyplot as plt


def create_nfl_boxplots(column: str, factor: str = "offense") -> None:
    """
    This function generates boxplots to visualize the distribution of NFL statistics
    for a specified column, distinguishing between offensive and defensive factors.
    The boxplots also differentiate teams based on whether they made the playoffs or not.

    Parameters
    ----------
    column: str
        The name of the column for which boxplots will be created
    factor: str, optional
        The factor to consider, either 'offense' or 'defense'

    Example
    -------
    >>> import pandas as pd
    >>> create_nfl_boxplots('yards_per_game', factor='defensive')
    """
    df = loader.combine_nfl_measure_tables(factor=factor)
    boxplot = df.boxplot(column=[column], by="made_playoffs")
    boxplot.get_figure().suptitle("")
    plt.savefig(f"plots/{column}_{factor}.png")
