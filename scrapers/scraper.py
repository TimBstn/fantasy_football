from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def get_driver(website: str, load_timeout: int = 3) -> webdriver.Chrome:
    """
    Get Selenium driver from website
    load for load_timeout seconds

    Parameters
    ----------
    website: str
        website to load data from
    load_timeout: int, optional
        timeout after which loading of website stops

    Returns
    -------
    webdriver.Chrome:
        webdriver
    """
    # options for selenium - don't show window and don't log information
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")

    # selenium driver - only load for 3 seconds
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(load_timeout)
    try:
        driver.get(website)
    except TimeoutException:
        driver.execute_script("window.stop();")
    return driver


def get_html(driver: webdriver.Chrome) -> BeautifulSoup:
    """
    import HTML of webpage into python

    Parameters
    ----------
    driver: webdriver.Chrome
        webdriver

    Returns
    -------
    BeautifulSoup:
        HTML of website
    """
    return BeautifulSoup(driver.page_source, "lxml")


def find_div(html: BeautifulSoup, id: str = None) -> BeautifulSoup:
    """
    Look in the children of html element and
    find the first div that matches the given criteria

    Parameters
    ----------
    html: BeautifulSoup
        html of website
    id: str, optional
        id of div in html

    Returns
    -------
    BeautifulSoup:
        div html
    """
    if id:
        return html.find("div", id=id)
    return html.find("div")


def find_span(html: BeautifulSoup, id: str = None) -> BeautifulSoup:
    """
    Look in the children of html element and
    find the first span that matches the given criteria

    Parameters
    ----------
    html: BeautifulSoup
        html of website
    id: str, optional
        id of span in html

    Returns
    -------
    BeautifulSoup:
        span html
    """
    if id:
        return html.find("span", id=id)
    return html.find("span")


def find_all_p(html: BeautifulSoup) -> list:
    """
    Look in the children of html element and
    find the p's that match the given criteria

    Parameters
    ----------
    html: BeautifulSoup
        html of website

    Returns
    -------
    list:
        list of all p's
    """
    return html.find_all("p")


def find_table(html: BeautifulSoup, id: str = None) -> BeautifulSoup:
    """
    Look in the children of html element and
    find the first table that matches the given criteria

    Parameters
    ----------
    html: BeautifulSoup
        html of website
    id: str, optional
        id of table in html

    Returns
    -------
    BeautifulSoup:
        table html
    """
    if id:
        return html.find("table", id=id)
    return html.find("table")


def find_all_rows(table: BeautifulSoup) -> list:
    """
    Look in the children of table element and
    find the all rows that match the given criteria

    Parameters
    ----------
    table: BeautifulSoup
        html of table

    Returns
    -------
    list:
        list of rows
    """
    return table.find_all("tr")


def find_table_header(table: BeautifulSoup) -> BeautifulSoup:
    """
    Look in the children of table element and
    find the table header that matches the given criteria

    Parameters
    ----------
    table: BeautifulSoup
        html of table

    Returns
    -------
    BeautifulSoup:
        html of table header
    """
    return table.find("th")


def find_all_table_cells(table: BeautifulSoup) -> list:
    """
    Look in the children of table element and
    find the table cells that match the given criteria

    Parameters
    ----------
    table: BeautifulSoup
        html of table

    Returns
    -------
    list:
        list of table cells
    """
    return table.find_all("td")


def find_href(html: BeautifulSoup) -> BeautifulSoup:
    """
    Look in the children of html element and
    find the first href element that matches the given criteria

    Parameters
    ----------
    html: BeautifulSoup
        html of website

    Returns
    -------
    BeautifulSoup:
        html of href
    """
    return html.find(href=True)
