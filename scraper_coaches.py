from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# options = Options()
# options.add_argument("--headless")

years = [i for i in range(2000, 2024)]

driver = webdriver.Chrome(
    # options=options
)
driver.get(f"https://www.pro-football-reference.com/years/2021/coaches.htm")

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

print(data_year)

driver.quit()
