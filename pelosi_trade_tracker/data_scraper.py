"""Scraping pelosi trading data from url provided below"""

import requests
from bs4 import BeautifulSoup

URL  = "https://www.capitoltrades.com/politicians/P000197"

try:
    r = requests.get(URL, timeout = 10)
except requests.Timeout:
    print("Request timed out")

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

for row in rows:
    ticker_header = row.find('a', class_='text-txt-interactive')
    print(ticker_header.get_text(strip = True))
