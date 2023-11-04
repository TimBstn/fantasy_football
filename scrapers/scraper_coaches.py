import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper


def scrape_coaches(years: list) -> pd.DataFrame:
    """
    Scrape coach data from
    https://www.pro-football-reference.com/years/{year}/coaches.htm

    Parameters
    ----------
    years: list
        list of years to scrape data for

    Returns
    -------
    DataFrame
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
        coaches = scraper.find_rows(table=table)
        for coach in coaches:
            # list for coach
            data_coach = list()
            data_coach.append(year)

            # stadium name - first column (is th)
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
            stats = scraper.find_table_cells(coach)
            for stat in stats:
                data_coach.append(stat.text)
            print(data_coach)
            if data_coach and len(data_coach) > 5:
                data.append(data_coach)
        driver.quit()

    df = pd.DataFrame(data=data, columns=header_mapping.header_coaches)
    return df


# coaches = df.drop_duplicates(subset=["coach_id"])
# coaches = coaches[
#     [
#         "coach_id",
#         "coach_name",
#         "games_career",
#         "wins_career",
#         "losses_career",
#         "ties_career",
#         "playoff_games_career",
#         "playoff_wins_career",
#         "playoff_losses_career",
#     ]
# ]
# coach_history = df[
#     [
#         "year",
#         "team_id",
#         "coach_id",
#         "games",
#         "wins",
#         "losses",
#         "ties",
#         "playoff_games",
#         "playoff_losses",
#         "remark",
#     ]
# ]

# coach_team = df.drop_duplicates(subset=["team_id", "coach_id"])
# coach_team = coach_team[
#     [
#         "team_id",
#         "coach_id",
#         "games_with_team",
#         "wins_with_team",
#         "losses_with_team",
#         "ties_with_team",
#         "playoff_games_team",
#         "playoff_wins_team",
#         "playoff_losses_team"
#     ]
# ]


# # write df
# df.to_excel(f"coaches.xlsx", index=False)
