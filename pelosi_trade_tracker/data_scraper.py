"""Scraping pelosi trading data from url provided below"""

import requests
from bs4 import BeautifulSoup

class DataScraper:
    """scrapes data from inputted URL, returns useful stock trading data"""
    def __init__(self):
        """trade_data holds data from parse_url"""
        self.trade_data = []
        self.name = ""
        self.name_set = False

    def want_politician_name(self, want_name = False):
        """if user wants name, will get it when parsing URL, else ignore"""
        if want_name is True:
            self.name_set = True

    def increment_url(self, url, page_num):
        """Increments page number of url to store all trades instead of only whats on first page"""
        new_url = url.split('page=')[0] + f"page={page_num + 1}"
        return new_url

    def process_rows(self, rows):
        """finds and appends useful data for each trade to trade list"""
        for row in rows:
            stock_name = row.find('a', class_ = 'text-txt-interactive')
            ticker = row.find('span', class_ = 'q-field')
            value = row.find('span', class_ = 'mt-1')
            trade_date = row.find_all('div', class_ = 'text-size-3 font-medium')[1]
            trade_year = row.find_all('div', class_ = 'text-size-2 text-txt-dimmer')[1]
            report_date = row.find('div', class_ = 'text-size-3 font-medium')
            report_year = row.find('div', class_ = 'text-size-2 text-txt-dimmer')

            order_type = None
            if row.find('span', class_ = 'tx-type--buy'):
                order_type = "Buy"
            elif row.find('span', class_ = 'tx-type--sell'):
                order_type = "Sell"
            elif row.find('span', class_ = 'tx-type--exchange'):
                order_type = "Exchange"
            elif row.find('span', class_ = "tx-type--receive"):
                order_type = "Receive"
            else:
                print("Unknown Order Type, request failed!")
                return

            self.trade_data.append({
                "stock_name": stock_name.get_text(strip=True) if stock_name else "N/A",
                "ticker": ticker.get_text(strip=True) if ticker else "N/A",
                "order_type": order_type,
                "value": value.get_text(strip=True) if value else "N/A",
                "trade_date": (
                    f"{trade_date.get_text(strip=True)} "
                    f"{trade_year.get_text(strip=True)}"
                ),
                "report_date": (
                    f"{report_date.get_text(strip=True)} "
                    f"{report_year.get_text(strip=True)}"
                )
            })

    def parse_url(self, url):
        """takes in URL input, stores stock trade data in trade_data"""
        try:
            r = requests.get(url, timeout = 5)
        except requests.Timeout:
            print("Request timed out")

        soup = BeautifulSoup(r.content, 'html.parser')

        if self.name_set is True:
            name = soup.find('h1').text
            self.name = name

        page_num_text = soup.find('p', class_ = 'hidden leading-7 sm:block')
        first_page = ''
        last_page = ''
        first_digit = False

        for char in page_num_text.get_text():
            if char.isdigit() and first_digit is False:
                first_digit = True
                first_page = char
            elif char.isdigit():
                last_page += char
        first_page = int(first_page) - 1
        last_page = int(last_page)

        while first_page < last_page:
            r = requests.get(self.increment_url(url, first_page), timeout = 5)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')
            self.process_rows(rows)
            first_page += 1

    def print_trade_data(self):
        """Prints the stored trade data. Name is only printed if user requests"""
        if self.name_set is True:
            name_output = "TRADER NAME: " + self.name
            print(name_output)
            for _ in name_output:
                print("-", end = '')
            print()
        for data in self.trade_data:
            print(
                f"Stock: {data['stock_name']}\n"
                f"Ticker: {data['ticker']}\n"
                f"Order Type: {data['order_type']}\n"
                f"Value: ${data['value']}\n"
                f"Date Traded: {data['trade_date']}\n"
                f"Date Reported: {data['report_date']}\n"
            )

def main():
    """Main"""
    # pelosi trades URL = https://www.capitoltrades.com/politicians/P000197?page=1
    get_pelosi_trades = DataScraper()
    get_pelosi_trades.want_politician_name(True)
    get_pelosi_trades.parse_url("https://www.capitoltrades.com/politicians/P000197?page=1")
    get_pelosi_trades.print_trade_data()

    # mcconnell trades URL= https://www.capitoltrades.com/politicians/M000355?page=1
    # get_mcconnell_trades = DataScraper()
    # get_mcconnell_trades.want_politician_name(True)
    # get_mcconnell_trades.parse_url("https://www.capitoltrades.com/politicians/M000355?page=1")
    # get_mcconnell_trades.print_trade_data()

    # mccaul trades URL = https://www.capitoltrades.com/politicians/M001157?page=1
    # 400 PAGES OF TRADES -- DO NOT RUN YET!!!

if __name__ == "__main__":
    main()
