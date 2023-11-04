import pandas as pd
import fantasy_football.utils.header_mapping as header_mapping
import fantasy_football.utils.logging as logging
import fantasy_football.scrapers.scraper as scraper
from typing import Tuple


def scrape_data() -> pd.DataFrame:
    """
    Scrape stadium data from
    https://www.pro-football-reference.com/stadiums/

    Returns
    -------
    DataFrame:
        stadium_id: str
            stadiums pro football reference id
        stadium_name: str
            name of stadium
        from: int
            year of first game in stadium
        to: int
            year of last game in stadium
        games: int
            number of games in stadium
        city: str
            city of stadium
        state: str
            state of stadium
        primary_team: str
            primary team/ user of stadium
        street: str
            street of stadium
        surface: str
            surface of stadium with years
        super_bowls: str
            super bowls played in stadium
    """
    # list for final DataFrame
    data = list()

    # website to scrape data from
    website = "https://www.pro-football-reference.com/stadiums/"

    # selenium driver
    driver = scraper.get_driver(website=website)

    # import HTML of webpage into python
    html = scraper.get_html(driver=driver)

    # get stadium table
    table = scraper.find_table(html=html, id="stadiums")

    # iterate over rows (stadiums)
    stadiums = scraper.find_all_rows(table=table)
    for stadium in stadiums:
        # list for stadium
        data_stadium = list()
        super_bowls = None

        # stadium name - first column (is th)
        stadium_th = scraper.find_table_header(table=stadium)
        stadium_name = stadium_th.text
        href = scraper.find_href(stadium_th)
        # open stadium specific website to scrape information
        logging.log(stadium_name)
        if href:
            # stadium id is his hyperlink handle
            stadium_id = href["href"][10:-4]
            data_stadium.append(stadium_id)
            data_stadium.append(stadium_name)
            stadium_href = (
                f"https://www.pro-football-reference.com/stadiums/{stadium_id}.htm"
            )
            driver_stadium = scraper.get_driver(website=stadium_href, load_timeout=6)
            html_stadium = scraper.get_html(driver=driver_stadium)
            info = scraper.find_div(html=html_stadium, id="info")
            meta = scraper.find_div(html=info, id="meta")
            ps = scraper.find_all_p(meta)
            # street information
            street = ps[0].text
            # get surface and super bowl information
            for p in ps:
                if p.text[:8] == "Surfaces":
                    surface = p.text.split(":")[1].strip()
                elif p.text[:11] == "Super Bowls":
                    super_bowls = p.text.split(":")[1].strip()
            driver_stadium.quit()
        else:
            street = None
            surface = None
            super_bowls = None
        stats = scraper.find_all_table_cells(stadium)
        for stat in stats:
            data_stadium.append(stat.text)
        data_stadium.append(street)
        data_stadium.append(surface)
        data_stadium.append(super_bowls)
        if data_stadium and len(data_stadium) > 5:
            data.append(data_stadium)
    driver.quit()
    df = pd.DataFrame(data=data, columns=header_mapping.header_stadiums)
    return df


def scrape_stadiums() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Scrape stadium data from
    https://www.pro-football-reference.com/stadiums/
    and put into SQL database format DataFrames

    Returns
    -------
    DataFrame:
        stadium_id: str
            stadiums pro football reference id
        stadium_name: str
            name of stadium
        from: int
            year of first game in stadium
        to: int
            year of last game in stadium
        games: int
            number of games in stadium
        city: str
            city of stadium
        state: str
            state of stadium
        street: str
            street of stadium
    DataFrame:
        stadium_id: str
            stadiums pro football reference id
        year: int
            seasons year
        surface: str
            surface of stadium
    DataFrame:
        super_bowl_id: str
            roman year of superbowl
        stadium_id: str
            stadiums pro football reference id
    """
    # df = scrape_data()
    df = pd.read_excel("stadiums_all.xlsx")

    # stadium mapping table
    stadiums = df[
        ["stadium_id", "stadium_name", "from", "to", "games", "city", "state", "street"]
    ]

    data_surface = list()
    for i, row in df[["stadium_id", "surface"]].iterrows():
        stadium_id = row["stadium_id"]
        surface = row["surface"]
        if not pd.isna(surface):
            surface = surface.split(",")
            for surf in surface:
                s_split = surf.split("(")
                surface_type = s_split[0].strip()
                years = s_split[1][:-1].split("-")
                if len(years) == 1:
                    data_surface.append([stadium_id, years[0], surface_type])
                else:
                    for y in range(int(years[0]), int(years[1]) + 1):
                        data_surface.append([stadium_id, y, surface_type])

    surface_history = pd.DataFrame(
        data_surface, columns=["stadium_id", "year", "surface"]
    )

    data_sb = list()
    for i, row in df[["stadium_id", "super_bowls"]].iterrows():
        stadium_id = row["stadium_id"]
        super_bowls = row["super_bowls"]
        if not pd.isna(super_bowls):
            sb_games = super_bowls.split(",")
            for sb in sb_games:
                data_sb.append([sb, stadium_id])

    super_bowl_history = pd.DataFrame(data_sb, columns=["super_bowl_id", "stadium_id"])
    return stadiums, surface_history, super_bowl_history
