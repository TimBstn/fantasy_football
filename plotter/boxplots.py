import fantasy_football.predictor.loader as loader
import matplotlib.pyplot as plt


def print_boxplots_offense(column):
    """

    Parameters
    ----------
    column: str
        column to show boxplot for
    """
    df_offense = loader.load_data_offense()
    boxplot = df_offense.boxplot(column=[column], by="made_playoffs")
    boxplot.get_figure().suptitle("")
    plt.savefig(f"plots/{column}.png")


def print_boxplots_defense(column):
    """

    Parameters
    ----------
    column: str
        column to show boxplot for
    """
    df_defense = loader.load_data_defense()
    boxplot = df_defense.boxplot(column=[column], by="made_playoffs")
    boxplot.get_figure().suptitle("")
    plt.savefig(f"plots/{column}_defense.png")
