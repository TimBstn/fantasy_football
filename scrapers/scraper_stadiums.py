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
    "Stadium_Name",
    "From",
    "To",
    "G",
    "City",
    "State",
    "Primary_Team",
    "Street",
    "Surface",
    "Super_Bowls",
]

# website to scrape data from
website = "https://www.pro-football-reference.com/stadiums/"

# selenium driver - only load for 2 seconds
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(2)
try:
    driver.get(website)
except TimeoutException:
    driver.execute_script("window.stop();")

# import HTML of webpage into python
soup = BeautifulSoup(driver.page_source, "lxml")

# get stadium table
table = soup.find("table", id="stadiums")

# list for final DataFrame
data = list()

# iterate over rows (stadiums)
stadiums = table.find_all("tr")
for stadium in stadiums:
    # list for stadium
    data_stadium = list()
    super_bowls = None

    # stadium name - first column (is th)
    stadium_name = stadium.find("th").text
    data_stadium.append(stadium_name)

    # open stadium specific website to scrape information
    href = stadium.find("a", href=True)
    if href:
        # stadium website
        stadium_href = website + href["href"][10:]
        driver_stadium = webdriver.Chrome(options=options)
        driver_stadium.set_page_load_timeout(2)
        try:
            driver_stadium.get(stadium_href)
        except TimeoutException:
            driver_stadium.execute_script("window.stop();")
        soup_stadium = BeautifulSoup(driver_stadium.page_source, "lxml")
        info = soup_stadium.find("div", id="info")
        meta = info.find("div", id="meta")
        ps = meta.find_all("p")
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
    stats = stadium.find_all("td")
    for stat in stats:
        data_stadium.append(stat.text)
    data_stadium.append(street)
    data_stadium.append(surface)
    data_stadium.append(super_bowls)
    if data_stadium and len(data_stadium) > 5:
        data.append(data_stadium)

driver.quit()

# write df
df = pd.DataFrame(data=data, columns=header)
df.to_excel(f"stadiums.xlsx", index=False)
