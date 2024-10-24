"""Scraping pelosi trading data from url provided below"""

import requests
from bs4 import BeautifulSoup

class DataScraper:
    """scrapes data from inputted URL, returns useful stock trading data"""

    def __init__(self):
        """trade_data holds data from parse_url"""
        self.trade_data = []

    def get_politician_name(self, url):
        """takes in URL input, outputs politician name associated with trades"""
        try:
            r = requests.get(url, timeout = 5)
        except requests.Timeout:
            print("Request timed out")

        soup = BeautifulSoup(r.content, 'html.parser')
        name = soup.find('h1').text
        return name

    def parse_url(self, url):
        """takes in URL input, stores stock trade data in trade_data"""
        try:
            r = requests.get(url, timeout = 5)
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

            order_type = None
            if row.find('span', class_ = 'tx-type--buy'):
                order_type = "Buy"
            elif row.find('span', class_ = 'tx-type--sell'):
                order_type = "Sell"
            elif row.find('span', class_ = 'tx-type--exchange'):
                order_type = "Exchange"
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

    def print_trade_data(self):
        """Prints the stored trade data."""
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
    # pelosi trades URL = https://www.capitoltrades.com/politicians/P000197
    # get_pelosi_trades = DataScraper()
    # name_output = "TRADER NAME: " + \
    #     get_pelosi_trades.get_politician_name(
    #         "https://www.capitoltrades.com/politicians/P000197"
    #     )
    # print(name_output)
    # for i in name_output:
    #     print("-", end = '')
    # print()
    # get_pelosi_trades.parse_url("https://www.capitoltrades.com/politicians/P000197")
    # get_pelosi_trades.print_trade_data()

    # mcconnell trades URL= https://www.capitoltrades.com/politicians/M000355
    get_mcconnell_trades = DataScraper()
    name_output = "TRADER NAME: " + \
        get_mcconnell_trades.get_politician_name(
            "https://www.capitoltrades.com/politicians/M000355"
        )
    print(name_output)
    for _ in name_output:
        print("-", end = '')
    print()
    get_mcconnell_trades.parse_url("https://www.capitoltrades.com/politicians/M000355")
    get_mcconnell_trades.print_trade_data()

if __name__ == "__main__":
    main()
