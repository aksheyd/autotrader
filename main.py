"""Make trades automatically using Nancy Pelosi's stock trades"""
import json
import requests

with open('config.json', encoding='utf-8') as f:
    api_key = json.load(f)['API_KEY']

def create_url(function, symbol):
    """Create a URL for the Alpha Vantage API"""
    return f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

def get_time_series_daily(symbol):
    """Get the daily time series for a stock"""
    url = create_url('TIME_SERIES_DAILY', symbol)
    response = requests.get(url, timeout=5)
    return response.json()

def get_time_series_intraday(symbol):
    """Get the intraday time series for a stock"""
    url = create_url('TIME_SERIES_INTRADAY', symbol)
    response = requests.get(url, timeout=5)
    return response.json()


def main():
    """Main"""
    symbol = 'AAPL'
    time_series = get_time_series_daily(symbol)
    print("Apple stock high on 2024-10-17:",
          time_series['Time Series (Daily)']['2024-10-17']['2. high'])

if __name__ == '__main__':
    main()
