import pandas as pd
import numpy as np
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
import fantasy_football.utils.mappings as mappings
from typing import Tuple


def scrape_data(years: list) -> pd.DataFrame:
    """
    Scrape standings data from
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
        team_id: str
            teams pro football reference id
        team_name: str
            teams name
        division_id:
            id of division
        division: str
            teams division
        odds_super_bowl: str
            pre season odds for winning super bowl
        odds_wins: str
            pre season odds for number of wins
        expected_wins: float
            expected wins that season
        expected_losses: float
            expected losses that season
        wins: int
            number of wins that season
        losses: int
            number of losses that season
        ties: int
            number of ties that season
        win_pct: float
            win percentage that season
        points_for: int
            points scored that season
        points_against: int
            points allowed that season
        points_diffential:
            points differential that season
        margin_of_victory: float
            (points scored - points allowed) / games
        strength_of_schedule: float
            average quality of schedule measured by SRS
        simple_rating_system: float
            team quality relative to average (0.0)
            SRS = MoV + SoS = OSRS + DFRS
        offensive_SRS: float
            team offense quality relative to average (0.0)
        defensive_SRS: float
            team defense quality relative to average (0.0)
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
        afc = scraper.find_table(html=html, id="AFC")
        nfc = scraper.find_table(html=html, id="NFC")
        conferences = [afc, nfc]

        # iterate over divisons teams
        for conference in conferences:
            standings = scraper.find_all_rows(table=conference)
            # iterate over rows (teams)
            for team in standings:
                # list for team
                data_team = list()
                data_team.append(year)

                # team name - first column (is th)
                team_th = scraper.find_table_header(table=team)
                if team_th:
                    team_name = team_th.text
                    if team_name[-1] in ["*", "+"]:
                        team_name = team_name[:-1]
                    href = scraper.find_href(team_th)
                else:
                    team_name = None
                if href:
                    # coach id is his hyperlink handle
                    team_id = href["href"][7:10]
                    data_team.append(team_id.upper())
                    data_team.append(team_name)
                    team_href = f"https://www.pro-football-reference.com/teams/{team_id}/{year}.htm"
                    driver_team = scraper.get_driver(website=team_href, load_timeout=6)
                    html_team = scraper.get_html(driver=driver_team)
                    meta = scraper.find_div(html=html_team, id="meta")
                    ps = scraper.find_all_p(meta)
                    for p in ps:
                        # print(p.text[:4])
                        if "Record" in p.text:
                            s1 = p.text.split("in")
                            s2 = s1[1].split("(")
                            division = s2[0].strip()
                            division_id = mappings.divisions[division]
                        elif "Preseason Odds" in p.text:
                            s1 = p.text.split("Super Bowl")
                            s2 = s1[1].split(";")
                            super_bowl_odds = int(s2[0].strip())
                            try:
                                s3 = s2[1].split(":")
                                wins_odds = float(s3[1].strip())
                            except:
                                wins_odds = None
                        elif "Expected" in p.text:
                            s1 = p.text.split(":")
                            s2 = s1[1].split("-")
                            expected_wins = float(s2[0].strip())
                            expected_losses = float(s2[1].strip())
                    data_team.append(division_id)
                    data_team.append(division)
                    data_team.append(super_bowl_odds)
                    data_team.append(wins_odds)
                    data_team.append(expected_wins)
                    data_team.append(expected_losses)
                    driver_team.quit()
                stats = scraper.find_all_table_cells(team)
                for stat in stats:
                    data_team.append(stat.text)
                if len(data_team) > 5:
                    if len(data_team) == 20:
                        data_team.insert(11, 0)
                    data.append(data_team)
        driver.quit()
    df = pd.DataFrame(data=data, columns=header_mapping.header_standings)
    df = df.dropna(subset=["team_name"])
    return df


def scrape_standings(years: list) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Scrape coach data from
    https://www.pro-football-reference.com/years/{year}/coaches.htm
    and put into SQL database format DataFrames

    Parameters
    ----------
    years: list
        list of years to scrape data for

    Returns
    -------
    DataFrame:
        team_id: str
            teams pro football reference id
        team_name: str
            teams name
        division_id: str
            id of division
        active: bool
            team is active
    DataFrame:
        division_id: str
            id of division
        division: str
            teams division
        conference: str
            teams conference
    DataFrame:
        year: int
            season year
        team_id: str
            teams pro football reference id
        odds_super_bowl: str
            pre season odds for winning super bowl
        odds_wins: str
            pre season odds for number of wins
        wins: int
            number of wins that season
        losses: int
            number of losses that season
        ties: int
            number of ties that season
        win_pct: float
            win percentage that season
        expected_wins: float
            expected wins that season
        expected_losses: float
            expected losses that season
        points_for: int
            points scored that season
        points_against: int
            points allowed that season
        points_diffential:
            points differential that season
        margin_of_victory: float
            (points scored - points allowed) / games
        strength_of_schedule: float
            average quality of schedule measured by SRS
        simple_rating_system: float
            team quality relative to average (0.0)
            SRS = MoV + SoS = OSRS + DFRS
        offensive_SRS: float
            team offense quality relative to average (0.0)
        defensive_SRS: float
            team defense quality relative to average (0.0)
    """
    # df = scrape_data(years=years)
    df = pd.read_excel("standings_all.xlsx")

    # teams table
    teams = df[["team_id", "team_name", "division_id"]]
    teams = teams.drop_duplicates(subset=["team_id"], keep="last")

    # division table
    division = df[["division_id", "division"]]
    division = division.drop_duplicates(subset=["division_id"])
    division["conference"] = division["division"].str[:3]

    # standings history
    standings_history = df[
        [
            "year",
            "team_id",
            "odds_super_bowl",
            "odds_wins",
            "wins",
            "losses",
            "ties",
            "win_pct",
            "expected_wins",
            "expected_losses",
            "points_for",
            "points_against",
            "points_diffential",
            "margin_of_victory",
            "strength_of_schedule",
            "simple_rating_system",
            "offensive_SRS",
            "defensive_SRS",
        ]
    ]
    return teams, division, standings_history
