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
    "Wins",
    "Losses",
    "Ties",
    "Win_Pct",
    "Points_For",
    "Points_Allowed",
    "Points_Diffential",
    "Margin_of_Victory",
    "Strength_of_Schedule",
    "Simple_Rating_System",
    "Offensive_SRS",
    "Defensive_SRS",
]

years = [i for i in range(2000, 2024)]
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
    afc = soup.find("table", id="AFC")
    nfc = soup.find("table", id="NFC")

    # list for final DataFrame
    data = list()

    # iterate over AFC teams
    afc_standings = afc.find_all("tr")
    for team in afc_standings:
        data_team = list()
        data_team.append(year)
        team_label = team.find("th")
        if team_label:
            team_name = team_label.text
            if team_name[-1] in ["*", "+"]:
                team_name = team_name[:-1]
        else:
            team_name = None
        data_team.append(team_name)
        team_stats = team.find_all("td")
        for stat in team_stats:
            data_team.append(stat.text)
        if len(data_team) > 5:
            if len(data_team) == 13:
                data_team.insert(4, 0)
            data.append(data_team)

    # iterate over NFC teams
    nfc_standings = nfc.find_all("tr")
    for team in nfc_standings:
        data_team = list()
        data_team.append(year)
        team_label = team.find("th")
        if team_label:
            team_name = team_label.text
            if team_name[-1] in ["*", "+"]:
                team_name = team_name[:-1]
        else:
            team_name = None
        data_team.append(team_name)
        team_stats = team.find_all("td")
        for stat in team_stats:
            data_team.append(stat.text)
        if len(data_team) > 5:
            if len(data_team) == 13:
                data_team.insert(4, 0)
            data.append(data_team)

    driver.quit()

    # write df
    df = pd.DataFrame(data=data, columns=header)
    df.to_excel(f"standings_{year}.xlsx", index=False)
