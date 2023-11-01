from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

games_year = {
    #2002: 17,
    #2003: 17,
    #2004: 17,
    #2005: 17,
    #2006: 17,
    #2007: 17,
    #2008: 17,
    #2009: 17,
    #2010: 17,
    2011: 17,
    2012: 17,
    2013: 17,
    2014: 17,
    2015: 17,
    2016: 17,
    2017: 17,
    2018: 17,
    2019: 17,
    2020: 17,
    2021: 18,
    2022: 18,
    2023: 8,
}
positions = [
    #"qb", 
    #"rb", 
    #"wr", 
    #"te", 
    #"k", 
    "dst", 
    "dl", 
    #"lb", 
    #"db"
    ]

for year, games in games_year.items():
    weeks = [i + 1 for i in range(games)]
    for pos in positions:
        pos_df = pd.DataFrame()
        for week in weeks:
            got_data = False
            while not got_data:
                try:
                    driver = webdriver.Chrome()
                    driver.get(
                        f"https://www.fantasypros.com/nfl/stats/{pos}.php?year={year}&roster=consensus&range=week&week={week}"
                    )

                    # Imports the HTML of the webpage into python
                    soup = BeautifulSoup(driver.page_source, "lxml")

                    # get table
                    table = soup.find("table", id="data")

                    # get header
                    header_row = table.find("thead")
                    header_labels = header_row.find("tr", class_="tablesorter-header")
                    header_texts = header_labels.find_all("th")
                    columns = [h.text for h in header_texts]
                    columns.insert(2, "Team")
                    columns.insert(0, "Week")
                    columns.insert(0, "Year")

                    # get player stats
                    player_list = []
                    tbody = table.find("tbody")
                    rows = tbody.find_all("tr")
                    for player in rows:
                        p = list()
                        p.append(year)
                        p.append(week)
                        stats = player.find_all("td")
                        for i, s in enumerate(stats):
                            if i == 1:
                                t = s.text.split("(", 1)
                                player = t[0].strip()
                                p.append(player)
                                team = t[1].split(")", 1)[0].strip()
                                p.append(team)
                            else:
                                p.append(s.text)
                        player_list.append(p)

                    df = pd.DataFrame(player_list, columns=columns)
                    pos_df = pd.concat([pos_df, df])
                    driver.quit()
                    got_data = True
                except:
                    pass
                
        pos_df.to_excel(f"{pos}_{year}.xlsx", index=False)
# qb_df.to_excel("qb.xlsx", index=False)
# rb_df.to_excel("rb.xlsx", index=False)
# wr_df.to_excel("wr.xlsx", index=False)
# te_df.to_excel("te.xlsx", index=False)
# k_df.to_excel("k.xlsx", index=False)
# dst_df.to_excel("dst.xlsx", index=False)
# dl_df.to_excel("dl.xlsx", index=False)
# lb_df.to_excel("lb.xlsx", index=False)
# db_df.to_excel("db.xlsx", index=False)
