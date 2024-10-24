"""Scraping pelosi trading data from url provided below"""

import requests
from bs4 import BeautifulSoup

URL = "https://www.capitoltrades.com/politicians/P000197"

try:
    r = requests.get(URL, timeout = 10)
except requests.Timeout:
    print("Request timed out")

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

for row in rows:
    stock_name = row.find('a', class_ = 'text-txt-interactive')
    ticker = row.find('span', class_ = 'q-field')
    value = row.find('span', class_ = 'mt-1')
    trade_date = row.find_all('div', class_ = 'text-size-3 font-medium')[1]
    trade_year = row.find_all('div', class_ = 'text-size-2 text-txt-dimmer')[1]
    report_date = row.find('div', class_ = 'text-size-3 font-medium')
    report_year = row.find('div', class_ = 'text-size-2 text-txt-dimmer')

    ORDER_TYPE = None
    if row.find('span', class_ = 'tx-type--buy'):
        ORDER_TYPE = "Buy"
    elif row.find('span', class_ = 'tx-type--sell'):
        ORDER_TYPE = "Sell"
    elif row.find('span', class_ = 'tx-type--exchange'):
        ORDER_TYPE = "Exchange"

    print(
        f"Stock: {stock_name.get_text(strip = True)}\n"
        f"Ticker: {ticker.get_text(strip = True)}\n"
        f"Order Type: {ORDER_TYPE}\n"
        f"Value: ${value.get_text(strip = True)}\n"

        f"Date Traded: {trade_date.get_text(strip = True)} "
        f"{trade_year.get_text(strip = True)}\n"

        f"Date Reported: {report_date.get_text(strip = True)} "
        f"{report_year.get_text(strip = True)}\n"
    )
