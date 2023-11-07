import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper


def scrape_data(years: list) -> pd.DataFrame:
    """
    Scrape playoff standings data from
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
        seat: int
            seat in conference
        wins: int
            number of wins that season
        losses: int
            number of losses that season
        ties: int
            number of ties that season
        position: str
            seat as string
        reason: str
            comment on seat
        made_playoffs: bool
            team made playoffs
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
        afc = scraper.find_table(html=html, id="afc_playoff_standings")
        nfc = scraper.find_table(html=html, id="nfc_playoff_standings")
        conferences = [afc, nfc]

        # iterate over teams
        for conference in conferences:
            standings = scraper.find_all_rows(table=conference)
            for seat, team in enumerate(standings):
                # list for team
                data_team = list()
                made_playoffs = False
                data_team.append(year)

                # team name - first column (is th)
                team_th = scraper.find_table_header(table=team)
                team_name = team_th.text
                href = scraper.find_href(team_th)
                if team_name:
                    if team_name[-1] in [")"]:
                        team_name = team_name[:-4]
                        made_playoffs = True
                else:
                    team_name = None
                if href:
                    team_id = href["href"][7:10]
                else:
                    team_id = None
                data_team.append(team_id)
                data_team.append(seat)
                team_stats = scraper.find_all_table_cells(team)
                for stat in team_stats:
                    data_team.append(stat.text)
                data_team.append(made_playoffs)
                if len(data_team) > 5:
                    data.append(data_team)

        driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_playoffs)
    return df


def scrape_playoffs(years: list) -> pd.DataFrame:
    """
    Scrape playoff standings data from
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
        team_id: str
            teams pro football reference id
        seat: int
            seat in conference
        position: str
            seat as string
        reason: str
            comment on seat
        made_playoffs: bool
            team made playoffs
    """
    df = scrape_data(years=years)
    playoff_history = df[
        ["year", "team_id", "seat", "position", "reason", "made_playoffs"]
    ]
    return playoff_history
