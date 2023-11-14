import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
from typing import Tuple


def scrape_data(years: list) -> pd.DataFrame:
    """
    Scrape game data from
    https://www.pro-football-reference.com/years/{year}/games.htm

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
        website = f"https://www.pro-football-reference.com/years/{year}/games.htm"

        # selenium driver
        driver = scraper.get_driver(website=website)

        # import HTML of webpage into python
        html = scraper.get_html(driver=driver)

        # get afc and nfc table
        table = scraper.find_table(html=html, id="games")
        tbody = table.find("tbody")

        # iterate over games
        games = scraper.find_all_rows(table=tbody)
        for game in games:
            # list for team
            data_game = list()
            data_game.append(year)

            # team name - first column (is th)
            week = scraper.find_table_header(table=game).text
            logging.log(week)
            data_game.append(week)
            game_stats = scraper.find_all_table_cells(game)
            for stat in game_stats:
                if "boxscore" in stat.text:
                    href_game = scraper.find_href(stat)
                    game_id = href_game["href"][11:-4]
                    data_game.append(game_id)

                    website_game = f"https://www.pro-football-reference.com/boxscores/{game_id}.htm"
                    got_data = False
                    while not got_data:
                        try:
                            # selenium driver game
                            driver_game = scraper.get_driver(
                                website=website_game, load_timeout=4
                            )
                            html = scraper.get_html(driver=driver_game)
                            score_box = html.find("div", class_="scorebox")
                            hrefs = score_box.find_all("a")
                            teams = list()
                            for h in hrefs:
                                if h["href"][:6] == "/teams":
                                    teams.append(h["href"][7:10].upper())
                            away_team = teams[0]
                            home_team = teams[1]
                            data_game.append(away_team)
                            data_game.append(home_team)
                            scores = score_box.find_all("div", class_="score")
                            for score in scores:
                                data_game.append(score.text)
                            scorebox_meta = score_box.find(
                                "div", class_="scorebox_meta"
                            )
                            scorebox_divs = scorebox_meta.find_all("div")
                            for i, div in enumerate(scorebox_divs):
                                if i == 0:
                                    s = div.text.split(" ", 1)
                                    game_day = s[0].strip()
                                    date = s[1].strip()
                                elif "Start Time" in div.text:
                                    time = div.text.split(":", 1)[1].strip()
                                elif "Stadium" in div.text:
                                    h = scraper.find_href(div)
                                    stadium_id = h["href"][10:-4]
                                elif "Attendance" in div.text:
                                    attendance = div.text.split(":", 1)[1].strip()
                                elif "Time of Game" in div.text:
                                    time_of_game = div.text.split(":", 1)[1].strip()
                            data_game.append(game_day)
                            data_game.append(date)
                            data_game.append(time)
                            data_game.append(stadium_id)
                            data_game.append(attendance)
                            data_game.append(time_of_game)

                            game_info = scraper.find_table(html, id="game_info")
                            infos = scraper.find_all_rows(table=game_info)
                            for info in infos:
                                try:
                                    info_label = scraper.find_table_header(
                                        table=info
                                    ).text
                                    info_value = scraper.find_all_table_cells(info)
                                    if "Won Toss" in info_label:
                                        won_toss = info_value[0].text.strip()
                                    elif "Roof" in info_label:
                                        roof = info_value[0].text.strip()
                                    elif "Vegas Line" in info_label:
                                        vegas_line = info_value[0].text.strip()
                                    elif "Over" in info_label:
                                        over_under = info_value[0].text.strip()
                                except:
                                    won_toss = None
                            data_game.append(won_toss)
                            data_game.append(roof),
                            data_game.append(vegas_line)
                            data_game.append(over_under)

                            ref_info = scraper.find_table(html, id="officials")
                            infos = scraper.find_all_rows(table=ref_info)
                            for info in infos:
                                try:
                                    info_label = scraper.find_table_header(
                                        table=info
                                    ).text
                                    info_value = scraper.find_all_table_cells(info)
                                    if "Referee" in info_label:
                                        referee = info_value[0].text.strip()
                                except:
                                    referee = None
                            data_game.append(referee)

                            team_stats = scraper.find_table(html, id="team_stats")
                            infos = scraper.find_all_rows(table=team_stats)
                            for info in infos:
                                info_label = scraper.find_table_header(table=info).text
                                info_value = scraper.find_all_table_cells(info)
                                for val in info_value:
                                    data_game.append(val.text.strip())
                            got_data = True
                        except:
                            pass

            if len(data_game) > 5:
                print(data_game)
                print(len(data_game))
                data.append(data_game)
            if len(data_game) == 52:
                raise NotImplementedError()
        driver.quit()
        pd.DataFrame(data=data, columns=header_mapping.header_games).to_excel(
            f"games_{year}.xlsx", index=False
        )

    # write df
    df = pd.DataFrame(data=data, columns=header_mapping.header_games)
    return df
