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
    ticker = row.find('a', class_ = 'text-txt-interactive')
    date = row.find('div', class_ = 'text-size-3 font-medium')
    bought = row.find('span', class_ = 'tx-type--buy')
    sold = row.find('span', class_ = 'tx-type--sell')
    exchange = row.find('span', class_ = 'tx-type--exchange')
    value = row.find('span', class_ = 'mt-1')

    if bought:
        print(
            "Stock: " + ticker.get_text(strip = True) + "\n" +
            "Order Type: Buy" + "\n" + 
            "Value: $" + value.get_text(strip = True) + "\n" + 
            "Date: " + date.get_text(strip = True),
            "\n"
        )
    elif sold:
        print(
            "Stock: " + ticker.get_text(strip = True) + "\n" +
            "Order Type: Sell" + "\n" + 
            "Value: $" + value.get_text(strip = True) + "\n" + 
            "Date: " + date.get_text(strip = True),
            "\n"
        )
    elif exchange:
        print(
            "Stock: " + ticker.get_text(strip = True) + "\n" +
            "Order Type: Exchange" + "\n" + 
            "Value: $" + value.get_text(strip = True) + "\n" + 
            "Date: " + date.get_text(strip = True),
            "\n"
        )
