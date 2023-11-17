import pandas as pd
import numpy as np


def combine_nfl_measure_tables(factor: str = "offense") -> pd.DataFrame:
    """
    This function combines different NFL measure tables, such as completion, scoring, returning, and punting,
    into a single DataFrame based on the specified factor ('offense' or 'defense').

    Parameters
    ----------
    factor: str, optional
        The factor to consider, either 'offense' or 'defense'

    Returns
    -------
    pd.DataFrame:
        A DataFrame combining various NFL measure tables related to the specified factor.

    Example
    -------
    >>> combined_df = combine_nfl_measure_tables('offense')
    """
    total = pd.read_excel(f"data/{factor}/total_{factor}.xlsx")
    if factor == "offense":
        cols = [
            "year",
            "team_id",
            "games",
            "total_yards",
            "offensive_plays",
            "yards_per_play",
            "turnovers_lost",
            "first_downs",
            "passes_completed",
            "passes_attempted",
            "net_yards_gained_per_pass",
            "yards_passing",
            "touchdowns_passing",
            "interceptions",
            "rushing_attempted",
            "yards_rushing",
            "rushing_yards_per_attempt",
            "touchdowns_rushing",
            "penalties_opponent",
            "yards_penalties_opponent",
            "pct_drives_ending_score",
            "pct_drives_ending_turnover",
        ]
    elif factor == "defense":
        cols = [
            "year",
            "team_id",
            "games",
            "points_against",
            "total_yards",
            "defensive_plays",
            "yards_per_play",
            "takeaways",
            "first_downs",
            "passes_completed",
            "passes_attempted",
            "yards_passing",
            "touchdowns_passing",
            "interceptions",
            "net_yards_gained_per_pass",
            "rushing_attempted",
            "yards_rushing",
            "touchdowns_rushing",
            "rushing_yards_per_attempt",
            "penalties_commited",
            "yards_penalties_commited",
            "first_downs_penalties_commited",
            "pct_drives_ending_score",
            "pct_drives_ending_turnover",
        ]
    total = total[cols]
    total["completion_pct"] = total["passes_completed"] / total["passes_attempted"]
    total["yards_per_game"] = total["total_yards"] / total["games"]
    total["touchdown_interception_ratio"] = (
        total["touchdowns_passing"] / total["interceptions"]
    )
    total["pass_run_ratio"] = total["passes_attempted"] / total["rushing_attempted"]

    scoring = pd.read_excel(f"data/{factor}/scoring_{factor}.xlsx")
    if factor == "offense":
        cols = [
            "year",
            "team_id",
            "total_touchdowns",
            "two_points_made",
            "two_points_attempted",
            "extra_points_made",
            "extra_points_attempted",
            "field_goals_made",
            "field_goals_attempted",
            "points_per_game",
        ]
        scoring = scoring[cols]
        scoring["field_goal_pct"] = (
            scoring["field_goals_made"] / scoring["field_goals_attempted"]
        )
        scoring["extra_point_pct"] = (
            scoring["extra_points_made"] / scoring["extra_points_attempted"]
        )
        scoring["two_point_pct"] = (
            scoring["two_points_made"] / scoring["two_points_attempted"]
        )
    elif factor == "defense":
        cols = [
            "year",
            "team_id",
            "total_touchdowns",
            "points_per_game",
        ]
        scoring = scoring[cols]
    total = total.merge(right=scoring, on=["year", "team_id"])

    returning = pd.read_excel(f"data/{factor}/returning_{factor}.xlsx")
    if factor == "offense":
        cols = [
            "year",
            "team_id",
            "punts_returned",
            "yards_per_punt_return",
            "kickoffs_returned",
            "yards_per_kickoff_return",
            "all_purpose_yards",
        ]
    elif factor == "defense":
        cols = [
            "year",
            "team_id",
            "punts_returned",
            "yards_per_punt_return",
            "kickoffs_returned",
            "yards_per_kickoff_return",
        ]
    returning = returning[cols]
    total = total.merge(right=returning, on=["year", "team_id"])

    punting = pd.read_excel(f"data/{factor}/punting_{factor}.xlsx")
    if factor == "offense":
        cols = [
            "year",
            "team_id",
            "punts_avg_yards",
            "punts_touchback_pct",
            "punts_inside_20_pct",
        ]
        punting = punting[cols]
        punting["punts_touchback_pct"] = (
            punting["punts_touchback_pct"].str.rstrip("%").astype("float") / 100.0
        )
        punting["punts_inside_20_pct"] = (
            punting["punts_inside_20_pct"].str.rstrip("%").astype("float") / 100.0
        )
    elif factor == "defense":
        cols = [
            "year",
            "team_id",
            "punts_avg_yards",
        ]
        punting = punting[cols]

    total = total.merge(right=punting, on=["year", "team_id"])

    conversion = pd.read_excel(f"data/{factor}/conversion_{factor}.xlsx")
    conversion = conversion[
        [
            "year",
            "team_id",
            "third_down_conversion_pct",
            "fourth_down_conversion_pct",
            "red_zone_conversion_pct",
        ]
    ]
    conversion["third_down_conversion_pct"] = (
        conversion["third_down_conversion_pct"].str.rstrip("%").astype("float") / 100.0
    )
    conversion["fourth_down_conversion_pct"] = (
        conversion["fourth_down_conversion_pct"].str.rstrip("%").astype("float") / 100.0
    )
    conversion["red_zone_conversion_pct"] = (
        conversion["red_zone_conversion_pct"].str.rstrip("%").astype("float") / 100.0
    )
    total = total.merge(right=conversion, on=["year", "team_id"])

    playoff_history = pd.read_excel("data/playoffs/playoff_history.xlsx")
    playoff_history = playoff_history[
        [
            "year",
            "team_id",
            "made_playoffs",
        ]
    ]
    total = total.merge(right=playoff_history, on=["year", "team_id"])

    return total
