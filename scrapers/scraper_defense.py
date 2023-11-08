import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
from typing import Tuple


def scrape_data(years: list, table_id: str, headers: list) -> pd.DataFrame:
    """
    Scrape team defense data from
    https://www.pro-football-reference.com/years/{year}/opp.htm

    Parameters
    ----------
    years: list
        list of years to scrape data for
    table_id: str
        id of table to be scraped
    headers: list
        list of column headers for DataFrame

    Returns
    -------
    DataFrame
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/opp.htm"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id=table_id)
        tbody = table.find("tbody")

        # iterate over teams
        standings = scraper.find_all_rows(table=tbody)
        for team in standings:
            # list for team
            data_team = list()
            data_team.append(year)

            # team name - first column (is th)
            team_th = scraper.find_table_header(table=team)
            rank = team_th.text
            data_team.append(rank)
            team_stats = scraper.find_all_table_cells(team)
            for i, stat in enumerate(team_stats):
                if i == 0:
                    href_team = scraper.find_href(stat)
                    if href_team:
                        team_id = href_team["href"][7:10].upper()
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=headers)
    return df


def scrape_defense(
    years: list,
) -> Tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    """
    Scrape offense data from
    https://www.pro-football-reference.com/years/{year}/opp.htm
    and put into SQL database format DataFrames

    Parameters
    ----------
    years: list
        list of years to scrape data for

    Returns
    -------
    DataFrame:
        year: int
            season year
        rank: int
            defensive rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        points_for: int
            points scored by opponent
        total_yards: int
            total offensive yards by opponent
        offensive_plays: int
            offensive plays = pass attempts + rush attempts + sacks
        yards_per_play: float
            yards per offensive play = (rush yards + pass yards) / offensive plays
        takeaways: int
            total number of takeovers
        fumbles_won: int
            total number of fumbles lost
        first_downs: int
            total number of first downs by opponent
        passes_completed: int
            passes completed by opponent
        passes_attempted: int
            passes attempts by opponent
        yards_passing: int
            yards gained by passing
        touchdowns_passing: int
            passing touchdowns
        interceptions: int
            interceptions caught
        net_yards_gained_per_pass: float
            net yards gained per pass attempt
        first_downs_passing: int
            total number of first downs by passing
        rushing_attempted: int
            rushing attempts
        yards_rushing: int
            yards gained by rushing
        touchdowns_rushing: int
            rushing touchdowns
        rushing_yards_per_attempt: float
            rushing yards gained
        first_downs_rushing: int
            total number of first downs by rushing
        penalties_commited: int
            penalties commited by opponents defense
        yards_penalties_commited: int
            yards gained by penalties opponent
        first_downs_penalties_commited: int
            total number of first downs by penalties opponents
        pct_drives_ending_score: float
            percent of drives ending in score
        pct_drives_ending_turnover:
            percent of drives ending in turnover
        expected_point_contr: float
            expected points contributed by total defense
    DataFrame:
        year: int
            season year
        rank: int
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        touchdowns_rushing: int
            rushing touchdowns by opponent
        touchdowns_passing: int
            passing touchdowns by opponent
        touchdowns_punt_returns: int
            touchdowns from punt returns by opponent
        touchdowns_kickoff_returns: int
            touchdowns from kickoff returns by opponent
        touchdowns_fumbles: int
            touchdowns from fumble returns by opponent
        touchdowns_interceptions: int
            touchdowns from interceptions by opponent
        touchdowns_other: int
            other touchdowns, p.e. blocked kicks or missed fieldgoals by opponent
        total_touchdowns: int
            total touchdowns by opponent
        two_points_made: int
            two point attempts made by opponent
        two_points_attempted: int
            two point attempts attempted by opponent
        defensive_two_points_made: int
            defensive two points made by opponent
        extra_points_made: int
            extra points made by opponent by opponent
        extra_points_attempted: int
            extra points attempted by opponent
        field_goals_made: int
            field goals made by opponent
        field_goals_attempted: int
            field goals attempted by opponent
        safeties: int
            safeties scored by opponent
        total_points: int
            total points scored by opponent
        points_per_game: float
            points per game scored by opponent
    DataFrame:
        year: int
            season year
        rank: int
            passing rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        passes_completed: int
            passes completed by opponent
        passes_attempted: int
            passes attempted by opponent
        completion_pct: float
            percentage of passes completed
        yards_passing: int
            yards gained by passing by opponent
        touchdowns_passing: int
            passing touchdowns by opponent
        touchdown_pct: float
            percentage of touchdowns thrown when attempting to pass
        interceptions: int
            interceptions caught
        passes_defended: int
            passed defended by defensive player
        interception_pct: float
            percentage of interceptions thrown when attempting to pass
        yards_gained_per_pass: float
            yards gained per pass attempt
        adjusted_yards_gained_per_pass: float
            adjusted yards gained per pass attempt
            (passing yards + 20 * passing touchdown - 45 * interception) / passes attempted
        yards_per_completion: float
            yards gained per completion
        yards_per_game: float
            yards gained per game
        rate: float
            quarterback rating
        sacks: int
            times sacked
        sacks_yards: int
            yards won due to sacks
        qb_hits: int
            quarterback hits
        tackles_for_loss: int
            tackles for loss
        sack_pct: float
            percentage of times sacked when attempting to pass
        net_yards_gained_per_pass: float
            net yards gained per pass attempt
        adjusted_net_yards_gained_per_pass: float
            net yards gained per pass attempt
            (passing yards - sack yards + 20 * passing touchdown - 45 * interception)
                / (passes attempted + sacks)
        expected_point_contr: float
            expected points contributed by passing defense
    DataFrame:
        year: int
            season year
        rank: int
            rushing rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        rushing_attempted: int
            rushing attempts by opponent
        yards_rushing: int
            yards gained by rushing
        touchdowns_rushing: int
            rushing touchdowns
        rushing_yards_per_attempt: float
            rushing yards gained per attempt
        rushing_yards_per_game: float
            rushing yards gained per game
        expected_point_contr: float
            expected points contributed by rushing defense
    DataFrame:
        year: int
            season year
        rank: int
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        punts_returned: int
            number of punts returned
        punt_return_yards: int
            yards from punt returns
        punt_return_touchdowns: int
            touchdowns from punt returns
        yards_per_punt_return: float
            averge yards per punt return
        kickoffs_returned: int
            number of kickoffs returned
        kickoff_return_yards: int
            yards from kickoff returns
        kickoff_return_touchdowns: int
            touchdowns from kickoff returns
        yards_per_kickoff_return: float
            averge yards per kickoff return
    DataFrame:
        year: int
            season year
        rank: int
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        field_goals_attempted: int
            field goals attempted by opponent
        field_goals_made: int
            field goals made by opponent
        field_goal_pct: float
            percentage of field goals made
        extra_points_attempted: int
            extra points attempted by opponent
        extra_points_made: int
            extra points made by opponent
        extra_points_pct: float
            extra point percentage
    DataFrame:
        year: int
            season year
        rank: int
            punting rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        punts: int
            number of punts
        punt_yards: int
            total yards punts
        punts_avg_yards: float
            average yard per punt
        punts_blocked: int
            times punt blocked
    DataFrame:
        year: int
            season year
        rank: int
            punting rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        third_downs_attempted: int
            total number of third down attempts by opponent
        third_downs_converted: int
            total number of third down converted by opponent
        third_down_conversion_pct: float
            third down conversion percentage
        fourth_downs_attempted: int
            total number of fourth down attempts by opponent
        fourth_downs_converted: int
            total number of fourth down converted by opponent
        fourth_down_conversion_pct: float
            fourth down conversion percentage
        red_zones_attempted: int
            total number of red zone attempts by opponent
        red_zones_converted: int
            total number of red zone attempts converted to touchdown by opponent
        red_zone_conversion_pct: float
            red zone to touchdown conversion percentage
    DataFrame:
        year: int
            season year
        rank: int
            punting rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        plays: int
            total number of plays (rush, pass, penalty) by opponent
        pct_drives_ending_score: float
            percent of drives ending in score
        pct_drives_ending_turnover: float
            percent of drives ending in turnover
        plays_avg: float
            average number of plays per drive
        yards_avg: float
            average number of yards per drive
        start: str
            average starting position
        time_avg: float
            average time of possesion per drive
        points_avg: float
            average number of points per drive
    """
    total_defense = scrape_data(
        years=years, table_id="team_stats", headers=header_mapping.header_defense
    )
    scoring_defense = scrape_data(
        years=years,
        table_id="team_scoring",
        headers=header_mapping.header_scoring_defense,
    )
    passing_defense = scrape_data(
        years=years, table_id="passing", headers=header_mapping.header_passing_defense
    )
    rushing_defense = scrape_data(
        years=years, table_id="rushing", headers=header_mapping.header_rushing_defense
    )
    returning_defense = scrape_data(
        years=years, table_id="returns", headers=header_mapping.header_returns_defense
    )
    kicking_defense = scrape_data(
        years=years, table_id="kicking", headers=header_mapping.header_kicking_defense
    )
    punting_defense = scrape_data(
        years=years, table_id="punting", headers=header_mapping.header_punting_defense
    )
    conversion_defense = scrape_data(
        years=years,
        table_id="team_conversions",
        headers=header_mapping.header_conversion_defense,
    )
    driving_defense = scrape_data(
        years=years, table_id="drives", headers=header_mapping.header_drives_defense
    )
    return (
        total_defense,
        scoring_defense,
        passing_defense,
        rushing_defense,
        returning_defense,
        kicking_defense,
        punting_defense,
        conversion_defense,
        driving_defense,
    )
