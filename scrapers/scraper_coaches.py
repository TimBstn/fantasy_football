import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
from typing import Tuple


def scrape_data(years: list) -> pd.DataFrame:
    """
    Scrape coach data from
    https://www.pro-football-reference.com/years/{year}/coaches.htm

    Parameters
    ----------
    years: list
        list of years to scrape data for

    Returns
    -------
    DataFrame:
        year: int
            season year
        coach_id: str
            coaches pro football reference id
        coach_name: str
            coaches name
        birthday: str
            coaches birthdaz
        birth_location: str
            coaches birth location
        team_id: str
            teams pro football reference id
        games: int
            number of games that season
        wins: int
            number of wins that season
        losses: int
            number of losses that season
        ties: int
            number of ties that season
        games_with_team: int
            number of games whit that team
        wins_with_team: int
            number of wins with that team
        losses_with_team: int
            number of losses with that team
        ties_with_team: int
            number of ties with that team
        games_career: int
            number of games in coaching career
        wins_career: int
            number of wins in coaching career
        losses_career: int
            number of losses in coaching career
        ties_career: int
            number of ties in coaching career
        playoff_games: int
            number of playoff games that season
        playoff_wins: int
            number of playoff wins that season
        playoff_losses: int
            number of playoff losses that season
        playoff_games_team: int
            number of playoffs games with that team
        playoff_wins_team: int
            number of playoff wins with that team
        playoff_losses_team: int
            number of playoff losses with that team
        playoff_games_career: int
            number of playoff games in coaching career
        playoff_wins_career: int
            number of playoff wins in coaching career
        playoff_losses_career: int
            number of playoff losses in coaching career
        remark: str
            comment
    """
    # iterate over years
    data = list()
    for year in years:
        logging.log(str(year))
        # website to scrape data from
        website = f"https://www.pro-football-reference.com/years/{year}/coaches.htm"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get coaches table
        table = scraper.find_table(html=html, id="coaches")

        # iterate over rows (coaches)
        coaches = scraper.find_all_rows(table=table)
        for coach in coaches:
            # list for coach
            data_coach = list()
            data_coach.append(year)

            # coach name - first column (is th)
            coach_th = scraper.find_table_header(table=coach)
            coach_name = coach_th.text
            href = scraper.find_href(coach_th)
            # open coach specific website to scrape information
            if href:
                # coach id is his hyperlink handle
                coach_id = href["href"][9:-4]
                data_coach.append(coach_id)
                data_coach.append(coach_name)
                coach_href = (
                    f"https://www.pro-football-reference.com/coaches/{coach_id}.htm"
                )
                driver_coach = scraper.get_driver(website=coach_href)
                html_coach = scraper.get_html(driver=driver_coach)
                # coach birthday and location
                birth = scraper.find_span(html=html_coach, id="necro-birth")
                birth = birth.text.strip()
                birth = birth.split("in", 1)
                birth_date = birth[0].strip()
                if len(birth) == 2:
                    birth_loc = birth[1].strip()
                else:
                    birth_loc = None
                data_coach.append(birth_date)
                data_coach.append(birth_loc)
                driver_coach.quit()
            stats = scraper.find_all_table_cells(coach)
            for i, stat in enumerate(stats):
                if i == 0:
                    href_team = scraper.find_href(stat)
                    if href_team:
                        team_id = href_team["href"][7:10].upper()
                    else:
                        team_id = None
                    data_coach.append(team_id)
                else:
                    data_coach.append(stat.text)
            if data_coach and len(data_coach) > 5:
                data.append(data_coach)
        driver.quit()

    df = pd.DataFrame(data=data, columns=header_mapping.header_coaches)
    return df


def scrape_coaches(years: list) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
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
        coach_id: str
            coaches pro football reference id
        coach_name: str
            coaches name
        games_career: int
            number of games in coaching career
        wins_career: int
            number of wins in coaching career
        losses_career
            number of losses in coaching career
        ties_career: int
            number of ties in coaching career
        playoff_games_career: int
            number of playoff games in coaching career
        playoff_wins_career: int
            number of playoff wins in coaching career
        playoff_losses_career: int
            number of playoff losses in coaching career
    DataFrame:
        year: int
            season year
        team_id: str
            teams pro football reference id
        coach_id: str
            coaches pro football reference id
        games: int
            number of games that season
        wins: int
            number of wins that season
        losses: int
            number of losses that season
        ties: int
            number of ties that season
        playoff_games: int
            number of playoff games that season
        playoff_wins: int
            number of playoff wins that season
        playoff_losses: int
            number of playoff losses that season
        remark: str
            comment
    DataFrame:
        team_id: st
            teams pro football reference id
        coach_id: str
            coaches pro football reference id
        games_with_team: int
            number of games whit that team
        wins_with_team: int
            number of wins with that team
        losses_with_team: int
            number of losses with that team
        ties_with_team: int
            number of ties with that team
        playoff_games_team: int
            number of playoffs games with that team
        playoff_wins_team: int
            number of playoff wins with that team
        playoff_losses_team: int
            number of playoff losses with that team
    """
    df = scrape_data(years=years)

    # coaches mapping table
    coaches = df.drop_duplicates(subset=["coach_id"])
    coaches = coaches[
        [
            "coach_id",
            "coach_name",
            "games_career",
            "wins_career",
            "losses_career",
            "ties_career",
            "playoff_games_career",
            "playoff_wins_career",
            "playoff_losses_career",
        ]
    ]

    # coach history per season table
    coach_history = df[
        [
            "year",
            "team_id",
            "coach_id",
            "games",
            "wins",
            "losses",
            "ties",
            "playoff_games",
            "playoff_wins",
            "playoff_losses",
            "remark",
        ]
    ]

    # coach history per team coached
    coach_team = df.drop_duplicates(subset=["team_id", "coach_id"])
    coach_team = coach_team[
        [
            "team_id",
            "coach_id",
            "games_with_team",
            "wins_with_team",
            "losses_with_team",
            "ties_with_team",
            "playoff_games_team",
            "playoff_wins_team",
            "playoff_losses_team",
        ]
    ]
    return coaches, coach_history, coach_team
