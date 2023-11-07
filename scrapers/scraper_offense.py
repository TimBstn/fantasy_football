import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
from typing import Tuple


def scrape_data_total_offense(years: list) -> pd.DataFrame:
    """
    Scrape team offense standings data from
    https://www.pro-football-reference.com/years/{year}/

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
            offensive rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        points_for: int
            points scored by team
        total_yards: int
            total offensive yards
        offensive_plays: int
            offensive plays = pass attempts + rush attempts + sacks
        yards_per_play: float
            yards per offensive play = (rush yards + pass yards) / offensive plays
        turnovers_lost: int
            total number of turnovers lost
        fumbles_lost: int
            total number of fumbles lost
        first_downs: int
            total number of first downs
        passes_completed: int
            passes completed
        passes_attempted: int
            passes attempts
        yards_passing: int
            yards gained by passing
        touchdowns_passing: int
            passing touchdowns
        interceptions: int
            interceptions thrown
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
        penalties_opponent: int
            penalties commited by opponents defense
        yards_penalties_opponent: int
            yards gained by penalties opponent
        first_downs_penalties_opponent: int
            total number of first downs by penalties opponents
        pct_drives_ending_score: float
            percent of drives ending in score
        pct_drives_ending_turnover:
            percent of drives ending in turnover
        expected_point_contr: float
            expected points contributed by total offense
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="team_stats")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_offense)
    return df


def scrape_data_scoring_offense(years: list) -> pd.DataFrame:
    """
    Scrape team scoring data from
    https://www.pro-football-reference.com/years/{year}/

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
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        touchdowns_rushing: int
            rushing touchdowns
        touchdowns_passing: int
            passing touchdowns
        touchdowns_punt_returns: int
            touchdowns from punt returns
        touchdowns_kickoff_returns: int
            touchdowns from kickoff returns
        touchdowns_fumbles: int
            touchdowns from fumble returns
        touchdowns_interceptions: int
            touchdowns from interceptions
        touchdowns_other: int
            other touchdowns, p.e. blocked kicks or missed fieldgoals
        total_touchdowns: int
            total touchdowns
        two_points_made: int
            two point attempts made
        two_points_attempted: int
            two point attempts attempted
        defensive_two_points_made: int
            defensive two points made
        extra_points_made: int
            extra points made
        extra_points_attempted: int
            extra points attempted
        field_goals_made: int
            field goals made
        field_goals_attempted: int
            field goals attempted
        safeties: int
            safeties scored
        total_points: int
            total points scored
        points_per_game: float
            points per game scored
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="team_scoring")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_scoring)
    return df


def scrape_data_passing_offense(years: list) -> pd.DataFrame:
    """
    Scrape team passing data from
    https://www.pro-football-reference.com/years/{year}/

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
            passing rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        passes_completed: int
            passes completed
        passes_attempted: int
            passes attempts
        completion_pct: float
            percentage of passes completed
        yards_passing: int
            yards gained by passing
        touchdowns_passing: int
            passing touchdowns
        touchdown_pct: float
            percentage of touchdowns thrown when attempting to pass
        interceptions: int
            interceptions thrown
        interception_pct: float
            percentage of interceptions thrown when attempting to pass
        longest_pass: int
            longest completed pass thrown
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
            yards lost due to sacks
        sack_pct: float
            percentage of times sacked when attempting to pass
        net_yards_gained_per_pass: float
            net yards gained per pass attempt
        adjusted_net_yards_gained_per_pass: float
            net yards gained per pass attempt
            (passing yards - sack yards + 20 * passing touchdown - 45 * interception)
                / (passes attempted + sacks)
        fourth_quarter_comebacks: int
            fourth quarter comeback
        game_winning_drives: int
            game winning drives (included OT)
        expected_point_contr: float
            expected points contributed by passing offense
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="passing")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_passing)
    return df


def scrape_data_rushing_offense(years: list) -> pd.DataFrame:
    """
    Scrape team rushing data from
    https://www.pro-football-reference.com/years/{year}/

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
            rushing rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        rushing_attempted: int
            rushing attempts
        yards_rushing: int
            yards gained by rushing
        touchdowns_rushing: int
            rushing touchdowns
        longest_rush: int
            longest rush
        rushing_yards_per_attempt: float
            rushing yards gained per attempt
        rushing_yards_per_game: float
            rushing yards gained per game
        fumbles_total: int
            total number of fumbles
        expected_point_contr: float
            expected points contributed by rushing offense
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="rushing")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_rushing)
    return df


def scrape_data_returning_offense(years: list) -> pd.DataFrame:
    """
    Scrape team returning data from
    https://www.pro-football-reference.com/years/{year}/

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
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        punts_returned: int
            number of punts returned
        punt_return_yards: int
            yards from punt returns
        touchdowns_punt_returns: int
            touchdowns from punt returns
        longest_punt_return: int
            longest punt return
        yards_per_punt_return: float
            averge yards per punt return
        kickoffs_returned: int
            number of kickoffs returned
        kickoff_return_yards: int
            yards from kickoff returns
        touchdowns_kickoff_returns: int
            touchdowns from kickoff returns
        longest_kickoff_return: int
            longest kickoff return
        yards_per_kickoff_return: float
            averge yards per kickoff return
        all_purpose_yards: int
            yards from ryshing, receiving, kick, punt, interceptions, fumble return
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="returns")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_returns)
    return df


def scrape_data_kicking_offense(years: list) -> pd.DataFrame:
    """
    Scrape team kicking data from
    https://www.pro-football-reference.com/years/{year}/

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
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        field_goals_attempted_0_19: int
            field goals attempted 19 yards and under
        field_goals_made_0_19: int
            field goals made 19 yards and under
        field_goals_attempted_20_29: int
            field goals attempted 20-29 yards
        field_goals_made_20_29: int
            field goals made 20-29 yards
        field_goals_attempted_30_39: int
            field goals attempted 30-39 yards
        field_goals_made_30_39: int
            field goals made 30-39 yards
        field_goals_attempted_40_49: int
            field goals attempted 40-49 yards
        field_goals_made_40_49: int
            field goals made 40-49 yards
        field_goals_attempted_50_plus: int
            field goals attempted 50 yards and more
        field_goals_made_50_plus: int
            field goals made 50 yards and more
        field_goals_attempted: int
            field goals attempted
        field_goals_made: int
            field goals made
        longest_field_goal: int
            yards of longest field goal
        field_goal_pct: float
            percentage of field goals made
        extra_points_attempted: int
            extra points attempted
        extra_points_made: int
            extra points made
        extra_points_pct: float
            extra point percentage
        kickoffs: int
            number of kickoffs
        kickoff_yards: int
            kickoff yards
        kickoff_touchbacks: int
            number of kickoff touchbacks
        touchback_pct: float
            percentage of touchbacks
        kickoff_avg_yards: float
            average yards of kickoff
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="kicking")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_kicking)
    return df


def scrape_data_punting_offense(years: list) -> pd.DataFrame:
    """
    Scrape team punting data from
    https://www.pro-football-reference.com/years/{year}/

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
        punt_return_yards_opponent: int
            punt return yards of opponent
        punt_net_yards: int
            punt net yards = punt yards - opponent returns - 20 * touchback
        punt_net_yards_per_punt: float
            ount net yards per punt including blocks
        longest_punt: int
            longest punt
        punts_touchback: int
            total number of touchbacks
        punts_touchback_pct: float
            percentage of punts resulting in touchback
        punts_inside_20: int
            punts inside opponent's 20 yard line
        punts_inside_20_pct: float
            percentage of punts downed inside opponent's 20 yard lone
        punts_blocked: int
            times punt blocked
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="punting")
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
                        team_id = href_team["href"][7:10]
                    else:
                        team_id = None
                    data_team.append(team_id)
                else:
                    data_team.append(stat.text)
            if len(data_team) > 5:
                data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_punting)
    return df


def scrape_offense(
    years: list,
) -> Tuple[
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
    https://www.pro-football-reference.com/years/{year}/
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
            offensive rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        points_for: int
            points scored by team
        total_yards: int
            total offensive yards
        offensive_plays: int
            offensive plays = pass attempts + rush attempts + sacks
        yards_per_play: float
            yards per offensive play = (rush yards + pass yards) / offensive plays
        turnovers_lost: int
            total number of turnovers lost
        fumbles_lost: int
            total number of fumbles lost
        first_downs: int
            total number of first downs
        passes_completed: int
            passes completed
        passes_attempted: int
            passes attempts
        yards_passing: int
            yards gained by passing
        touchdowns_passing: int
            passing touchdowns
        interceptions: int
            interceptions thrown
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
        penalties_opponent: int
            penalties commited by opponents defense
        yards_penalties_opponent: int
            yards gained by penalties opponent
        first_downs_penalties_opponent: int
            total number of first downs by penalties opponents
        pct_drives_ending_score: float
            percent of drives ending in score
        pct_drives_ending_turnover:
            percent of drives ending in turnover
        expected_point_contr: float
            expected points contributed by total offense
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
            rushing touchdowns
        touchdowns_passing: int
            passing touchdowns
        touchdowns_punt_returns: int
            touchdowns from punt returns
        touchdowns_kickoff_returns: int
            touchdowns from kickoff returns
        touchdowns_fumbles: int
            touchdowns from fumble returns
        touchdowns_interceptions: int
            touchdowns from interceptions
        touchdowns_other: int
            other touchdowns, p.e. blocked kicks or missed fieldgoals
        total_touchdowns: int
            total touchdowns
        two_points_made: int
            two point attempts made
        two_points_attempted: int
            two point attempts attempted
        defensive_two_points_made: int
            defensive two points made
        extra_points_made: int
            extra points made
        extra_points_attempted: int
            extra points attempted
        field_goals_made: int
            field goals made
        field_goals_attempted: int
            field goals attempted
        safeties: int
            safeties scored
        total_points: int
            total points scored
        points_per_game: float
            points per game scored
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
            passes completed
        passes_attempted: int
            passes attempts
        completion_pct: float
            percentage of passes completed
        yards_passing: int
            yards gained by passing
        touchdowns_passing: int
            passing touchdowns
        touchdown_pct: float
            percentage of touchdowns thrown when attempting to pass
        interceptions: int
            interceptions thrown
        interception_pct: float
            percentage of interceptions thrown when attempting to pass
        longest_pass: int
            longest completed pass thrown
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
            yards lost due to sacks
        sack_pct: float
            percentage of times sacked when attempting to pass
        net_yards_gained_per_pass: float
            net yards gained per pass attempt
        adjusted_net_yards_gained_per_pass: float
            net yards gained per pass attempt
            (passing yards - sack yards + 20 * passing touchdown - 45 * interception)
                / (passes attempted + sacks)
        fourth_quarter_comebacks: int
            fourth quarter comeback
        game_winning_drives: int
            game winning drives (included OT)
        expected_point_contr: float
            expected points contributed by passing offense
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
            rushing attempts
        yards_rushing: int
            yards gained by rushing
        touchdowns_rushing: int
            rushing touchdowns
        longest_rush: int
            longest rush
        rushing_yards_per_attempt: float
            rushing yards gained per attempt
        rushing_yards_per_game: float
            rushing yards gained per game
        fumbles_total: int
            total number of fumbles
        expected_point_contr: float
            expected points contributed by rushing offense
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
        longest_punt_return: int
            longest punt return
        yards_per_punt_return: float
            averge yards per punt return
        kickoffs_returned: int
            number of kickoffs returned
        kickoff_return_yards: int
            yards from kickoff returns
        kickoff_return_touchdowns: int
            touchdowns from kickoff returns
        longest_kickoff_return: int
            longest kickoff return
        yards_per_kickoff_return: float
            averge yards per kickoff return
        all_purpose_yards: int
            yards from ryshing, receiving, kick, punt, interceptions, fumble return
    DataFrame:
        year: int
            season year
        rank: int
            returning rank
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        field_goals_attempted_0_19: int
            field goals attempted 19 yards and under
        field_goals_made_0_19: int
            field goals made 19 yards and under
        field_goals_attempted_20_29: int
            field goals attempted 20-29 yards
        field_goals_made_20_29: int
            field goals made 20-29 yards
        field_goals_attempted_30_39: int
            field goals attempted 30-39 yards
        field_goals_made_30_39: int
            field goals made 30-39 yards
        field_goals_attempted_40_49: int
            field goals attempted 40-49 yards
        field_goals_made_40_49: int
            field goals made 40-49 yards
        field_goals_attempted_50_plus: int
            field goals attempted 50 yards and more
        field_goals_made_50_plus: int
            field goals made 50 yards and more
        field_goals_attempted: int
            field goals attempted
        field_goals_made: int
            field goals made
        longest_field_goal: int
            yards of longest field goal
        field_goal_pct: float
            percentage of field goals made
        extra_points_attempted: int
            extra points attempted
        extra_points_made: int
            extra points made
        extra_points_pct: float
            extra point percentage
        kickoffs: int
            number of kickoffs
        kickoff_yards: int
            kickoff yards
        kickoff_touchbacks: int
            number of kickoff touchbacks
        touchback_pct: float
            percentage of touchbacks
        kickoff_avg_yards: float
            average yards of kickoff
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
        punt_return_yards_opponent: int
            punt return yards of opponent
        punt_net_yards: int
            punt net yards = punt yards - opponent returns - 20 * touchback
        punt_net_yards_per_punt: float
            ount net yards per punt including blocks
        longest_punt: int
            longest punt
        punts_touchback: int
            total number of touchbacks
        punts_touchback_pct: float
            percentage of punts resulting in touchback
        punts_inside_20: int
            punts inside opponent's 20 yard line
        punts_inside_20_pct: float
            percentage of punts downed inside opponent's 20 yard lone
        punts_blocked: int
            times punt blocked
    """
    total_offense = scrape_data_total_offense(years=years)
    scoring_offense = scrape_data_scoring_offense(years=years)
    passing_offense = scrape_data_passing_offense(years=years)
    rushing_offense = scrape_data_rushing_offense(years=years)
    returning_offense = scrape_data_returning_offense(years=years)
    kicking_offense = scrape_data_kicking_offense(years=years)
    punting_offense = scrape_data_punting_offense(years=years)
    return (
        total_offense,
        scoring_offense,
        passing_offense,
        rushing_offense,
        returning_offense,
        kicking_offense,
        punting_offense,
    )
