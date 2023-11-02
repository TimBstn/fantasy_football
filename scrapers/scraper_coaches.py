from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

options = Options()
options.add_argument("--headless")

years = [i for i in range(2000, 2024)]
header = [
    "Coach",
    "Team",
    "Season Games",
    "Season Wins",
    "Season Losses",
    "Season Ties",
    "Games w/ Team",
    "Wins w/ Team",
    "Losses w/ Team",
    "Ties w/ Team",
    "Games Career",
    "Wins Career",
    "Losses Career",
    "Ties Career",
    "Season Playoff Games",
    "Season Playoff Wins",
    "Season Playoff Losses",
    "Playoff Games w/ Team",
    "Playoff Wins w/ Team",
    "Playoff Losses w/ Team",
    "Playooff Games Career",
    "Playoff Wins Career",
    "Playoff Losses Career",
    "Remark",
]

for year in years:
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.pro-football-reference.com/years/{year}/coaches.htm")

    # Imports the HTML of the webpage into python
    soup = BeautifulSoup(driver.page_source, "lxml")

    # get table
    table = soup.find("table", id="coaches")

    data_year = list()
    # get rows
    coaches = table.find_all("tr")
    for coach in coaches:
        data_coach = list()
        coach_name = coach.find("th").text
        data_coach.append(coach_name)
        stats = coach.find_all("td")
        for stat in stats:
            data_coach.append(stat.text)
        if data_coach and len(data_coach) > 5:
            data_year.append(data_coach)

    driver.quit()

    # write df
    df_year = pd.DataFrame(data=data_year, columns=header)
    df_year.to_excel(f"coaches_{year}.xlsx", index=False)
