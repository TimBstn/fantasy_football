from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd

# options for selenium - don't show window and don't log information
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")

# header for final DataFrame
header = [
    "Year",
    "Team",
    "Seat",
    "Wins",
    "Losses",
    "Ties",
    "Position",
    "Reason",
    "Made_Playoffs",
]

years = [i for i in range(2003, 2024)]
for year in years:
    # website to scrape data from
    website = f"https://www.pro-football-reference.com/years/{year}/"

    # selenium driver - only load for 2 seconds
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(2)
    try:
        driver.get(website)
    except TimeoutException:
        driver.execute_script("window.stop();")

    # import HTML of webpage into python
    soup = BeautifulSoup(driver.page_source, "lxml")

    # get afc table
    afc = soup.find("table", id="afc_playoff_standings")
    nfc = soup.find("table", id="nfc_playoff_standings")

    # list for final DataFrame
    data = list()

    # iterate over AFC teams
    afc_standings = afc.find_all("tr")
    for seat, team in enumerate(afc_standings):
        data_team = list()
        made_playoffs = False
        data_team.append(year)
        team_label = team.find("th")
        if team_label:
            team_name = team_label.text
            if team_name[-1] in [")"]:
                team_name = team_name[:-4]
                made_playoffs = True
        else:
            team_name = None
        data_team.append(team_name)
        data_team.append(seat)
        team_stats = team.find_all("td")
        for stat in team_stats:
            data_team.append(stat.text)
        data_team.append(made_playoffs)
        if len(data_team) > 5:
            data.append(data_team)

    # iterate over NFC teams
    nfc_standings = nfc.find_all("tr")
    for seat, team in enumerate(nfc_standings):
        data_team = list()
        made_playoffs = False
        data_team.append(year)
        team_label = team.find("th")
        if team_label:
            team_name = team_label.text
            if team_name[-1] in [")"]:
                team_name = team_name[:-4]
                made_playoffs = True
        else:
            team_name = None
        data_team.append(team_name)
        data_team.append(seat)
        team_stats = team.find_all("td")
        for stat in team_stats:
            data_team.append(stat.text)
        data_team.append(made_playoffs)
        if len(data_team) > 5:
            data.append(data_team)

    driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header)
    df.to_excel(f"playoffs_{year}.xlsx", index=False)
