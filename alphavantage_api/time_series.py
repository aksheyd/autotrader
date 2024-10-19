"""File to fetch data based on user input, relies on helper_functions.py to make URL"""
import requests

from .helper_functions import create_url

class TimeSeries:
    """Fetches data from the website and returns based on selected stock ticker"""
    def __init__(self):
        pass

    def get_time_series_daily(self, symbol):
        """Get the daily time series for a stock"""
        url = create_url('TIME_SERIES_DAILY', symbol)
        response = requests.get(url, timeout=5)
        return response.json()

    def get_time_series_intraday(self, symbol):
        """Get the intraday time series for a stock"""
        url = create_url('TIME_SERIES_INTRADAY', symbol)
        response = requests.get(url, timeout=5)
        return response.json()
