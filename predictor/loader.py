import pandas as pd
import numpy as np


def load_data_offense():
    """
    Combine Offense DataFrames to one master DataFrame
    """
    total_offense = pd.read_excel("data/offense/total_offense.xlsx")
    total_offense = total_offense[
        [
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
    ]
    total_offense["completion_pct"] = (
        total_offense["passes_completed"] / total_offense["passes_attempted"]
    )
    total_offense["yards_per_game"] = (
        total_offense["total_yards"] / total_offense["games"]
    )
    total_offense["touchdown_interception_ratio"] = (
        total_offense["touchdowns_passing"] / total_offense["interceptions"]
    )
    total_offense["pass_run_ratio"] = (
        total_offense["passes_attempted"] / total_offense["rushing_attempted"]
    )

    scoring_offense = pd.read_excel("data/offense/scoring_offense.xlsx")
    scoring_offense = scoring_offense[
        [
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
    ]
    scoring_offense["field_goal_pct"] = (
        scoring_offense["field_goals_made"] / scoring_offense["field_goals_attempted"]
    )
    scoring_offense["extra_point_pct"] = (
        scoring_offense["extra_points_made"] / scoring_offense["extra_points_attempted"]
    )
    scoring_offense["two_point_pct"] = (
        scoring_offense["two_points_made"] / scoring_offense["two_points_attempted"]
    )
    total_offense = total_offense.merge(right=scoring_offense, on=["year", "team_id"])

    returning_offense = pd.read_excel("data/offense/returning_offense.xlsx")
    returning_offense = returning_offense[
        [
            "year",
            "team_id",
            "punts_returned",
            "yards_per_punt_return",
            "kickoffs_returned",
            "yards_per_kickoff_return",
            "all_purpose_yards",
        ]
    ]
    total_offense = total_offense.merge(right=returning_offense, on=["year", "team_id"])

    punting_offense = pd.read_excel("data/offense/punting_offense.xlsx")
    punting_offense = punting_offense[
        [
            "year",
            "team_id",
            "punts_avg_yards",
            "punts_touchback_pct",
            "punts_inside_20_pct",
        ]
    ]
    total_offense = total_offense.merge(right=punting_offense, on=["year", "team_id"])

    conversion_offense = pd.read_excel("data/offense/conversion_offense.xlsx")
    conversion_offense = conversion_offense[
        [
            "year",
            "team_id",
            "third_down_conversion_pct",
            "fourth_down_conversion_pct",
            "red_zone_conversion_pct",
        ]
    ]
    total_offense = total_offense.merge(
        right=conversion_offense, on=["year", "team_id"]
    )

    playoff_history = pd.read_excel("data/playoffs/playoff_history.xlsx")
    playoff_history = playoff_history[
        [
            "year",
            "team_id",
            "made_playoffs",
        ]
    ]
    total_offense = total_offense.merge(right=playoff_history, on=["year", "team_id"])

    return total_offense


def load_data_defense():
    """
    Combine Defense DataFrames to one master DataFrame
    """
    total_defense = pd.read_excel("data/defense/total_defense.xlsx")
    total_defense = total_defense[
        [
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
    ]
    total_defense["completion_pct"] = (
        total_defense["passes_completed"] / total_defense["passes_attempted"]
    )
    total_defense["yards_per_game"] = (
        total_defense["total_yards"] / total_defense["games"]
    )
    total_defense["touchdown_interception_ratio"] = (
        total_defense["touchdowns_passing"] / total_defense["interceptions"]
    )

    scoring_defense = pd.read_excel("data/defense/scoring_defense.xlsx")
    scoring_defense = scoring_defense[
        [
            "year",
            "team_id",
            "total_touchdowns",
            "points_per_game",
        ]
    ]
    total_defense = total_defense.merge(right=scoring_defense, on=["year", "team_id"])

    returning_defense = pd.read_excel("data/defense/returning_defense.xlsx")
    returning_defense = returning_defense[
        [
            "year",
            "team_id",
            "punts_returned",
            "yards_per_punt_return",
            "kickoffs_returned",
            "yards_per_kickoff_return",
        ]
    ]
    total_defense = total_defense.merge(right=returning_defense, on=["year", "team_id"])

    punting_defense= pd.read_excel("data/defense/punting_defense.xlsx")
    punting_defense = punting_defense[
        [
            "year",
            "team_id",
            "punts_avg_yards",
        ]
    ]
    total_defense = total_defense.merge(right=punting_defense, on=["year", "team_id"])

    conversion_defense = pd.read_excel("data/defense/conversion_defense.xlsx")
    conversion_defense = conversion_defense[
        [
            "year",
            "team_id",
            "third_down_conversion_pct",
            "fourth_down_conversion_pct",
            "red_zone_conversion_pct",
        ]
    ]
    total_defense = total_defense.merge(
        right=conversion_defense, on=["year", "team_id"]
    )

    playoff_history = pd.read_excel("data/playoffs/playoff_history.xlsx")
    playoff_history = playoff_history[
        [
            "year",
            "team_id",
            "made_playoffs",
        ]
    ]
    total_defense = total_defense.merge(right=playoff_history, on=["year", "team_id"])


    return total_defense
